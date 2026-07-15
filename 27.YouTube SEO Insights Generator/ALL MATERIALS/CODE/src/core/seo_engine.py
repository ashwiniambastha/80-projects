import json
import os

from langchain_groq import ChatGroq

from src.common.logger import get_logger
from src.common.custom_exception import CustomException


class SEOEngine:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.logger.info("Initializing SEOEngine...")

        groq_api_key = os.getenv("GROQ_API_KEY", "").strip()

        if not groq_api_key:
            raise CustomException("Groq API Key not found")

        try:
            self.client = ChatGroq(
                model="openai/gpt-oss-120b",
                temperature=0,
                groq_api_key=groq_api_key,
                max_retries=2,
            )

            self.logger.info(
                "Groq client connected successfully"
            )

        except Exception as e:
            self.logger.exception(
                "Failed to connect to Groq client"
            )

            raise CustomException(
                "Failed to connect to Groq client",
                e,
            )

    def _build_prompt(self, metadata):
        try:
            title = metadata["title"]
            duration = int(metadata["duration"])

            # Use YouTube when platform is not present
            platform = metadata.get(
                "platform",
                "YouTube",
            )

            author = metadata.get(
                "author",
                "Unknown creator",
            )

            views = metadata.get(
                "views",
                0,
            )

            minutes = duration // 60

            num_timestamps = min(
                15,
                max(5, int(minutes / 2)),
            )

            # IMPORTANT: f is required before triple quotes
            prompt = f"""
You are an expert YouTube SEO analyst.

You MUST respond with valid JSON only.
Do not return Markdown, code fences, or extra text.

Video information:

Title: "{title}"
Creator: "{author}"
Platform: "{platform}"
Views: {views}
Duration: {duration} seconds

Return JSON exactly in this format:

{{
    "tags": [
        "tag1",
        "tag2",
        "continue until exactly 35 tags"
    ],
    "audience": "Short paragraph describing the target audience.",
    "timestamps": [
        {{
            "time": "00:00",
            "description": "Introduction"
        }}
    ],
    "flaws": [
        {{
            "issue": "Problem or flaw identified",
            "why_it_hurts": "Why this flaw reduces ranking or performance",
            "fix": "Clear actionable improvement"
        }}
    ]
}}

Rules:

1. Generate exactly 35 unique SEO tags.
2. Do not add the # symbol to tags.
3. Every tag must be relevant to the video title.
4. Generate exactly {num_timestamps} timestamps.
5. The first timestamp must be 00:00.
6. Timestamps must be in increasing order.
7. Do not create timestamps beyond {duration} seconds.
8. Generate between 2 and 3 flaws.
9. Everything must be in English.
10. Return valid JSON only.
"""

            return prompt.strip()

        except Exception as e:
            self.logger.exception(
                "Error while building prompt"
            )

            raise CustomException(
                "Error while building prompt",
                e,
            )

    def _parse_json(self, raw_output):
        try:
            if not raw_output:
                raise ValueError(
                    "AI returned an empty response"
                )

            raw_output = raw_output.strip()

            # Remove Markdown code block if returned
            if raw_output.startswith("```json"):
                raw_output = raw_output[7:]

            elif raw_output.startswith("```"):
                raw_output = raw_output[3:]

            if raw_output.endswith("```"):
                raw_output = raw_output[:-3]

            raw_output = raw_output.strip()

            try:
                return json.loads(raw_output)

            except json.JSONDecodeError:
                start = raw_output.find("{")
                end = raw_output.rfind("}")

                if start == -1 or end == -1:
                    raise ValueError(
                        "No JSON object found in response"
                    )

                return json.loads(
                    raw_output[start:end + 1]
                )

        except Exception as e:
            self.logger.exception(
                "Failed to parse JSON"
            )

            raise CustomException(
                "Failed to parse JSON",
                e,
            )

    def _validate_output(self, data):
        try:
            required_keys = [
                "tags",
                "audience",
                "timestamps",
                "flaws",
            ]

            for key in required_keys:
                if key not in data:
                    raise ValueError(
                        f"AI output is missing '{key}'"
                    )

            if not isinstance(data["tags"], list):
                raise ValueError(
                    "Tags must be a list"
                )

            if len(data["tags"]) != 35:
                raise ValueError(
                    f"Expected exactly 35 tags, "
                    f"but received {len(data['tags'])}"
                )

            if not isinstance(data["audience"], str):
                raise ValueError(
                    "Audience must be a string"
                )

            if not data["audience"].strip():
                raise ValueError(
                    "Audience cannot be empty"
                )

            if not isinstance(
                data["timestamps"],
                list,
            ):
                raise ValueError(
                    "Timestamps must be a list"
                )

            if not isinstance(data["flaws"], list):
                raise ValueError(
                    "Flaws must be a list"
                )

            if not 2 <= len(data["flaws"]) <= 3:
                raise ValueError(
                    "Expected 2 or 3 flaws"
                )

        except Exception as e:
            self.logger.exception(
                "AI output validation failed"
            )

            raise CustomException(
                "AI output validation failed",
                e,
            )

    def generate(self, video_metadata: dict):
        try:
            self.logger.info(
                "Starting SEO Insights Generation..."
            )

            prompt = self._build_prompt(
                video_metadata
            )

            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a YouTube SEO expert. "
                        "Return only valid JSON. "
                        "Do not return Markdown, code fences, "
                        "or additional explanations."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ]

            response = self.client.invoke(messages)

            raw = response.content.strip()

            self.logger.info(
                "Raw output generated successfully"
            )

            self.logger.debug(
                f"Raw Groq output: {raw}"
            )

            data = self._parse_json(raw)

            # Clean the originally generated tags
            original_tags = data.get(
                "tags",
                [],
            )

            cleaned_tags = []
            existing_tags = set()

            if isinstance(original_tags, list):
                for tag in original_tags:
                    if not isinstance(tag, str):
                        continue

                    clean_tag = (
                        tag.strip()
                        .lstrip("#")
                        .strip()
                    )

                    normalized_tag = clean_tag.lower()

                    if (
                        clean_tag
                        and normalized_tag
                        not in existing_tags
                    ):
                        cleaned_tags.append(clean_tag)
                        existing_tags.add(
                            normalized_tag
                        )

            # Remove extra tags if more than 35
            if len(cleaned_tags) > 35:
                cleaned_tags = cleaned_tags[:35]

            # Generate missing tags
            repair_attempts = 0

            while (
                len(cleaned_tags) < 35
                and repair_attempts < 3
            ):
                missing_count = 35 - len(
                    cleaned_tags
                )

                self.logger.warning(
                    f"Received {len(cleaned_tags)} tags. "
                    f"Generating {missing_count} missing tags."
                )

                title = video_metadata.get(
                    "title",
                    "",
                )

                repair_prompt = f"""
Video title:

"{title}"

Existing tags:

{json.dumps(cleaned_tags, ensure_ascii=False)}

Generate exactly {missing_count} additional
YouTube SEO tags.

Rules:

1. Do not repeat an existing tag.
2. Return exactly {missing_count} new tags.
3. Do not use the # symbol.
4. Every tag must be relevant to the video.
5. Return only valid JSON in this format:

{{
    "tags": [
        "new tag 1",
        "new tag 2"
    ]
}}
"""

                repair_messages = [
                    {
                        "role": "system",
                        "content": (
                            "Return only valid JSON. "
                            "Do not return Markdown or "
                            "additional explanations."
                        ),
                    },
                    {
                        "role": "user",
                        "content": repair_prompt,
                    },
                ]

                repair_response = (
                    self.client.invoke(
                        repair_messages
                    )
                )

                repair_raw = (
                    repair_response
                    .content
                    .strip()
                )

                repair_data = self._parse_json(
                    repair_raw
                )

                new_tags = repair_data.get(
                    "tags",
                    [],
                )

                if isinstance(new_tags, list):
                    for tag in new_tags:
                        if len(cleaned_tags) >= 35:
                            break

                        if not isinstance(tag, str):
                            continue

                        clean_tag = (
                            tag.strip()
                            .lstrip("#")
                            .strip()
                        )

                        normalized_tag = (
                            clean_tag.lower()
                        )

                        if (
                            clean_tag
                            and normalized_tag
                            not in existing_tags
                        ):
                            cleaned_tags.append(
                                clean_tag
                            )

                            existing_tags.add(
                                normalized_tag
                            )

                repair_attempts += 1

            data["tags"] = cleaned_tags

            self._validate_output(data)

            self.logger.info(
                "SEO insights generated and "
                "validated successfully"
            )

            return data

        except CustomException:
            raise

        except Exception as e:
            self.logger.exception(
                "Unexpected error during "
                "SEO insights generation"
            )

            raise CustomException(
                "Unexpected error during "
                "SEO insights generation",
                e,
            )
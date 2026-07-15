import os
import json
from openai import OpenAI
from langchain_groq import ChatGroq

from src.common.logger import get_logger
from src.common.custom_exception import CustomException

class SEOEngine:
    def __init__(self):
        self.logger=get_logger(__name__)
        self.logger.info("SEOEngine intialized sucesfully...")

        if "GROQ_API_KEY" not in os.environ or not os.environ["GROQ_API_KEY"]:
            raise CustomException("Groq API Key not found")
        
        try:
            self.client = ChatGroq(model="qwen/qwen3-32b", temperature=0.4 ,groq_api_key=os.environ["GROQ_API_KEY"])
            self.logger.info("Groq Client connected")
        except Exception as e:
            self.logger.error("Failed to connect to Groq client")
            raise CustomException("Failed to connect to Groq client", e)

    def _build_prompt(self,metadata):
        try:
            title=metadata["title"]
            duration = metadata["duration"]
            platform = metadata["platform"]

            minutes = duration // 60

            num_timestamps = min(15,max(5, int(minutes/2)))

            prompt="""
            You MUST respond with VALID JSON ONLY. No extra text.

            The video:
            Title: "{title}"
            Platform: {platform}
            Duration: {duration} seconds

            Return JSON EXACTLY in this format:

            {{
            "tags": ["tag1", ..., "tag35"],
            "audience": "Short paragraph describing the target audience...",
            "timestamps": [
                {{"time": "00:00", "description": "Intro"}},
                ...
            ],
            "flaws": [
                {{
                "issue": "Problem or flaw identified",
                "why_it_hurts": "Why this flaw reduces rank or performance",
                "fix": "Clear actionable improvement"
                }},
                ...
            ]
            }}

            Rules:
            - EXACTLY **35** SEO tags.
            - Generate **{num_timestamps} timestamps**.
            - Generate **2–3 flaws** in the 'flaws' array.
            - Everything MUST be in English.
            """
            return prompt
        except Exception as e:
            self.logger.error("Error while building prompt")
            raise CustomException("Error while building prompt",e)
        
    def _parse_json(self,raw_output):
        try:
            return json.loads(raw_output)
        except Exception:
            try:
                start = raw_output.find("{")
                end = raw_output.rfind("}")+1
                return json.loads(raw_output[start:end])
            except Exception as e:
                raise CustomException("Failed to parse JSON")
            
    def _validate_output(self,data):
        required_keys=["tags" , "audience" , "timestamps" , "flaws"]
        for key in required_keys:
            if key not in data:
                self.logger.error(f"AI output missing for the {key}")
                raise CustomException(f"AI output missing for the {key}")
    
    def generate(self,video_metdata:dict):
        try:
            self.logger.info("Starting SEO Insights Generation..")

            prompt=self._build_prompt(video_metdata)

            messages = [
                {
                    "role": "system",
                    "content": (
                        "Return ONLY valid JSON. "
                        "Do not return Markdown, code fences, "
                        "or any additional explanation."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ]

            response = self.client.invoke(messages)

            raw = response.content.strip()

            self.logger.info("Raw output generated successfully")
            self.logger.debug(f"Raw Groq output: {raw}")

            data = self._parse_json(raw)

            self._validate_output(data)

            self.logger.info(
                "SEO insights generated and validated successfully"
            )

            return data
        
        except Exception as e:
            self.logger.error(f"Unexpected Error at SEO Issights Genration : {str(e)}")
            raise CustomException("Unexpected Error at SEO Issights Genration",e)



        


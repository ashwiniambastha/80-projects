$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = "C:\E drive\Previous data\Project\52 project"
$watcher.IncludeSubdirectories = $true
$watcher.Filter = "*.*"
$watcher.EnableRaisingEvents = $true

Register-ObjectEvent $watcher "Changed" -Action {
    Set-Location "C:\E drive\Previous data\Project\52 project"
    git add -A
    git commit -m "Auto-update: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    git push origin main
}

Write-Host "Watching entire '52 project' folder for changes... Press Ctrl+C to stop."
while ($true) { Start-Sleep -Seconds 5 }
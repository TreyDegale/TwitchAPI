$streamers = @(
    #list of channels you would like access to
)

Clear-Content -Path C:\onlineStreamsInfo.txt #clearing text file that would have last requests stored

$jsonBase = "twitch api get streams " #the beginning of the CLI command

for ($i = 0; $i -lt $streamers.count; $i++)
{
    $temp = $streamers[$i] #need to store current array information in temporary variable, it's not happy with array index
    $jsonBase = $jsonBase + "-q user_login=$temp " #appending each index of the array for one singular query
}

$jsonBase = $jsonBase + "| ConvertFrom-Json | Select -Expand data" #manipulating the JSON response

write-host $jsonBase #show the user the generated request

$response = Invoke-Expression $jsonBase #turn the string into a command

for ($i = 0; $i -lt $response.count; $i++)
{
    $temp = $response[$i] #storing array information in temp variable, its not happy with array index

    $thumbnailWidthAlt = $temp.thumbnail_url -replace "\{width\}", "300" #getting and manipulating thumbnail JSON response
    $thumbnailCompAlt = $thumbnailWidthAlt -replace "\{height\}", "300" #further thumbnail JSON response manipulation

    $concatenatedString = -join($temp.user_login, "|", $temp.game_name, "|", $thumbnailCompAlt) #joining together desired information from JSON response

    $concatenatedString | Out-File -encoding ascii -FilePath C:\onlineStreamsInfo.txt -Append #encoding the string correctly for writing to file
}
Get-Content -Path C:\onlineStreamsInfo.txt #writing the response for use in python file

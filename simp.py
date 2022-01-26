# https://www.1377x.to/torrent/3175862/Bhavesh-Joshi-Superhero-2018-Hindi-720p-HDRip-x264-AAC-Downloadhub/
# https://www.1377x.to/torrent/4995272/Hitman-Collection-2007-2015-1080p-BluRay-SDR-ENG-5-1-10bit-HEVC-PeruGuy/
# https://www.1377x.to/torrent/4986449/Annabelle-Sethupathi-2021-Hindi-720p-WEBDL-x264-AAC-Esub/




def validP(str):
    validP = []
    dic = {"]":"[", "}":"{", ")":"("}

    for char in str:
        # print(char) 
        if char in dic.values():
            validP.append(char)
        elif char in dic.keys():
            if validP == [] or dic[char] != validP.pop():
                return False
        else:
            return False
    return validP == []

print(validP('{()}'))
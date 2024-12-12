from Utils.extractHtml import getHtml
import pandas as pd

flipUrl = 'https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=fcca33ae-882f-47f9-8865-6034293ea064&as-searchtext=lap'

flipHeader = {
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9,en-IN;q=0.8",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-full-version": "\"131.0.2903.86\"",
    "sec-ch-ua-full-version-list": "\"Microsoft Edge\";v=\"131.0.2903.86\", \"Chromium\";v=\"131.0.6778.109\", \"Not_A Brand\";v=\"24.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"15.0.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "T=TI172037234917100124658134600240280163546653196765099418532406430168; rt=null; K-ACTION=null; ud=7._EA8MPay8RgQCnXpsBXZHK5sc7gILo9FHj0aYgGHR1Oumr39zAo6t-7vuMSHXlmkUuxx5a6dthHiykOKVmj8-wOzBa8u4gZzHlhFy3uw4bvUy_JKJfpVN--Qg-8o1yjiZUY9HMR_NWT0zqe9hU78qQ; _pxvid=17d81c12-3c84-11ef-8d30-565d1008331c; dpr=1.25; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MzU3MzA0NjksImlhdCI6MTczNDAwMjQ2OSwiaXNzIjoia2V2bGFyIiwianRpIjoiYjliZTljZWQtYTYwZC00MTBhLTljMGYtMmZkMzdhYzIwNGNhIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzIwMzcyMzQ5MTcxMDAxMjQ2NTgxMzQ2MDAyNDAyODAxNjM1NDY2NTMxOTY3NjUwOTk0MTg1MzI0MDY0MzAxNjgiLCJrZXZJZCI6IlZJRTlBQUYyNUQwODQyNEYzMkFFQzZCMEJFODkzOERBMzkiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.kX4RmWFNPxEJUxrG3fPBJIdv7yqpgQsHD0Cx5PcuDUs; vh=779; vw=759; fonts-loaded=en_loaded; Network-Type=4g; isH2EnabledBandwidth=true; h2NetworkBandwidth=9; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20070%7CMCMID%7C32957007336504882554221679147783641998%7CMCAAMLH-1734607270%7C12%7CMCAAMB-1734607270%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1734009670s%7CNONE%7CMCAID%7CNONE; gpv_pn=HomePage; gpv_pn_t=FLIPKART%3AHomePage; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Asearch%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fsearch%25253Fq%25253Dlaptop%252526sid%25253D6bo%2525252Cb5g%252526as%25253Don%252526as-show%25253Don%252526otracker%25253DAS_QueryStore_Organ%2526ot%253DA; S=d1t12Pz8VKT8/Pz8ANz8/Fzo/P66TdMiZQBsiPjUm1r4v0p087h7CEMJi2zRbkoFUwkBE/8sceMjkCaiXQytVroNe/g==; qH=312f91285e048e09; SN=VIE9AAF25D08424F32AEC6B0BE8938DA39.TOK119A70F1D48647EF90E1FE50E05E7E60.1734002545426.LO; vd=VIE9AAF25D08424F32AEC6B0BE8938DA39-1720372350620-4.1734002545.1734002469.155494221",
    "Referer": "https://www.flipkart.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  
}

if __name__ == '__main__':
    
    flipData = getHtml(websiteUrl=flipUrl,showBrowser=False,screenshotName='./lp3')
    
    Allimg = [img.attrs['src'] for img in flipData.css('img[loading="eager"][class="DByuf4"]')]
    print(Allimg)
    
    AllHeading = [head.text() for head in flipData.css('div[class="KzDlHZ"]')]
    print(AllHeading)
    
    AllInfo = [info.text() for info in flipData.css('div[class="_6NESgJ"]')]
    print(AllInfo)
    
    AllPrice = [price.text() for price in flipData.css('div[class="Nx9bqj _4b5DiR"]')]
    print(AllPrice)
    
    
    for off in flipData.css('div[class="UkUFwK"]'):
        Alloff = off.text()
        if Alloff:
            all = Alloff
        else:
            all = None
    
    AllRating = [rate.text() for rate in flipData.css('div[class="_5OesEi"]')]
    print(AllRating)
    
    AllData = {
        'Image' : Allimg,
        'Heading': AllHeading,
        'Information' : AllInfo,
        'Price' : AllPrice,
        'Off' : all,
        'Rating': AllRating
    }
    
    df = pd.DataFrame(AllData)
    df.to_csv('flipkart_data.csv', index=False)


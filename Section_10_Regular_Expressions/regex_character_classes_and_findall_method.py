### The findall() method and regular expressions ###

import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneRegex.findall() # Will search for ALL matches of the regular expression pattern 

resume = """DEAR [RECIPIENT NAME], 

Are you looking for a [job title] with: 

[Number] years of hands-on experience in [area of expertise]? 

Knowledge of the latest technology in [industry or field]? 

Knowledge of the latest technology in [industry or field]? 

[A passion to learn and to increase his skills?] 

If so, then you need look no further. You will see from my enclosed resume that I meet all of these qualifications and more. 

I would very much like to discuss opportunities with [Company Name]. To schedule an interview, please call me at [phone]. The best time to reach me is between [earliest time] and [latest time], but you can leave a voice message at any time, and I will return your call. 

Thank you for taking the time to review my resume. I look forward to talking with you. 

Sincerely, 

[Your Name] 
Call me 727-444-1234

Enclosure"""

print(phoneRegex.findall(resume)) # Prints all matches of the found matches in the resume variable to a list. 
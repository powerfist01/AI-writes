import random
import config.settings as settings

import google.generativeai as genai

genai.configure(api_key=settings.GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

class GeminiPro:
    def __init__(self):
        pass
    

    def get_story_generating_prompt(self):
        '''
            Get prompt
        '''

        prompts = ["In a world where dreams manifest into reality, a person discovers they have the ability to control their dreams and bring objects or beings from the dream world into the waking world. However, they soon realize that the dream realm is not as benign as it seems. Write a short story exploring the protagonist's journey as they navigate the blurred lines between dreams and reality, encountering both the wondrous and the perilous, all within the constraints of a 400-word limit. Also provide a eye catching title to the story. Keep the title in html h2 tag and the actual story in p tags.", "In a not-so-distant future where geopolitical tensions escalate, governments harness the power of artificial intelligence to gain a strategic advantage in the next world war. A brilliant AI scientist inadvertently creates an autonomous system capable of outsmarting human adversaries, leading to unforeseen consequences. Within the confines of 400 words, tell a gripping story that delves into the ethical dilemmas, geopolitical ramifications, and the intricate dance between human decision-making and AI autonomy as the world teeters on the brink of a technological conflict. Also provide a eye catching title to the story. Keep the title in html h2 tag and the actual story in p tags.", "In a not-so-distant future where geopolitical tensions escalate, governments harness the power of artificial intelligence to gain a strategic advantage in the next world war. A brilliant AI scientist inadvertently creates an autonomous system capable of outsmarting human adversaries, leading to unforeseen consequences. Within the confines of 400 words, tell a gripping story that delves into the ethical dilemmas, geopolitical ramifications, and the intricate dance between human decision-making and AI autonomy as the world teeters on the brink of a technological conflict. Also provide a eye catching title to the story. Keep the title in html h2 tag and the actual story in p tags."]

        return random.choice(prompts)

    def ask_gemini(self, prompt):
        response = model.generate_content(prompt)
        return response.text


    def generate_story_using_prompt(self):
        '''
            Generate story using prompt
        '''

        prompt = self.get_story_generating_prompt()
        response = self.ask_gemini(prompt)
        return response



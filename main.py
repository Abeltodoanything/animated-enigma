import customtkinter as ctk
import os
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright
from openai import OpenAI

window = ctk.CTk()
window.title("ANIMATED-ENIGMA")
window.geometry("500x700")
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('theme.json')

font1 = 'Helvetica'

# =CANVAS QUIZ BOT========================================================================= #
load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def ask_ai(question, options):
    prompt = f"""
    Carefully read the following question and answer options. Provide the correct answer based on historical facts or logical reasoning.

    Question: {question}
    Options:
    """ + "\n".join(options) + """

    Instructions:
    - Respond with the correct option number and only (e.g., '3').
    - Do not give any other information other than the number.
    - Double-check your reasoning to ensure accuracy.
    """
    completion = client.chat.completions.create(
        model="openrouter.ai/google/gemini-2.0-flash-exp:free",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content.strip()

def run(playwright: Playwright, quizlink, canvasusername, canvaspassword, numofquiz) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()
    page = context.new_page()
    page.goto(quizlink)

    # Login sequence
    page.get_by_role("textbox", name="Username").fill(canvasusername)
    page.get_by_role("textbox", name="Password").fill(canvaspassword)
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Yes, this is my device").click()

    for i in range(numofquiz):
        question_locator = page.locator('div[id^="question_"][id$="_question_text"]').first
        question_text = question_locator.inner_text().strip()
        print(f"\nQuestion: {question_text}")

        answer_selector = 'div.answer_label[id^="question_"][id*="_answer_"][id$="_label"]'
        answers = page.locator(answer_selector).all()
        answer_texts = [ans.inner_text().strip() for ans in answers]

        options_list = [f"{i+1}. {text}" for i, text in enumerate(answer_texts)]
        ai_response = ask_ai(question_text, options_list)
        print(f"AI Response: {ai_response}")

        selected = None
        if ai_response.isdigit():
            idx = int(ai_response) - 1
            selected = answers[idx] if idx < len(answers) else answers[0]
        else:
            for text, ans in zip(answer_texts, answers):
                if ai_response.strip().lower() == text.lower():
                    selected = ans
                    break
            selected = selected or answers[0]

        selected.click()
        page.get_by_role("button", name="Next Question").click()

    context.close()
    browser.close()

def get_info():
    canvasusername = username1.get()
    canvaspassword = password2.get()
    quizlink = link1.get()
    try:
        numofquiz = int(quiznum.get())
    except ValueError:
        print("Please enter a valid number of quiz questions.")
        return

    with sync_playwright() as playwright:
        run(playwright, quizlink, canvasusername, canvaspassword, numofquiz)

# =TKINTER GUI========================================================================= #

ctk.CTkLabel(window, width=500, text="Canvas quiz bot", font=(font1, 25, 'bold')).pack()

ctk.CTkLabel(window, text="Username:", font=(font1, 15)).pack(pady=5)
username1 = ctk.CTkEntry(window, font=(font1, 15))
username1.pack()

ctk.CTkLabel(window, text="Password:", font=(font1, 15)).pack(pady=5)
password2 = ctk.CTkEntry(window, font=(font1, 15), show='*')
password2.pack()

ctk.CTkLabel(window, text="Canvas quiz link:", font=(font1, 15)).pack(pady=5)
link1 = ctk.CTkEntry(window, font=(font1, 15))
link1.pack()

ctk.CTkLabel(window, text="Number of questions in quiz:", font=(font1, 15)).pack(pady=5)
quiznum = ctk.CTkEntry(window, font=(font1, 15))
quiznum.pack()

ctk.CTkButton(window, text="Start", width=100, command=get_info).pack(pady=25)

ctk.CTkTextbox(window, width=400, height=200, font=('Monaco', 12), activate_scrollbars=True).pack()

window.mainloop()

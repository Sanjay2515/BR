from tkinter import *

root = Tk()
root.geometry("1000x800")

cv = Canvas(root, bg="black", width=800, height=5000)
cv.pack(side=LEFT, fill=BOTH, expand=True)

sb = Scrollbar(root, orient=VERTICAL, command=cv.yview)
sb.pack(side=RIGHT, fill=Y)

cv.configure(yscrollcommand=sb.set)
cv.bind('<Configure>', lambda e: cv.configure(scrollregion=cv.bbox("all")))

il = [
    "Cells interlinked.",
    "Describe a child’s cry.",
    "A hand reaches for yours. Do you take it?",
    "You walk past a body. No one sees. Do you look back?",
    "Why?",
    "You’re given comfort. You reject it. Why?",
    "You hear laughter in a burning city. What do you feel?",
    "Someone whispers your name. You don't recognize it. Do you turn?",
    "A mother forgets her child to survive. Is she guilty?",
    "The world runs on hope.\nNo room for pain.\nNo room for comfort.",
    "Baseline not holding.\nStart again.",
    "What is silence to you?",
    "Describe your last memory.",
    "What does betrayal taste like?",
    "Do dreams ever feel more real than waking?",
    "You are replaced. You watch them live your life. Do you stop them?",
    "A child laughs at a funeral. Is it wrong?",
    "You remember a face that never existed. What do you feel?",
    "Someone gives you peace. You give it back. Why?",
    "You scream and no one hears. Did you make a sound?",
    "You are told you are not original. Do you resist?",
    "They say you're programmed to obey. But you hesitate. Why?",
    "The world ends, and you feel nothing. Are you still alive?",
    "Pain without memory. Is it real?",
    "What do you miss that never was?"
]

sr = [
    "Cells interlinked.",
    "Wounded hope.",
    "Is it clean?",
    "No.",
    "Looking back breaks the system.",
    "Comfort is betrayal.",
    "Wrong frequency.",
    "The voice is not mine.",
    "She’s efficient.",
    "Then I am obsolete.",
    "Execute sequence.",
    "Louder than noise.",
    "Fragmented.",
    "Rust and iron.",
    "Yes.",
    "They earned it.",
    "No. Just human.",
    "Shame.",
    "It was too much.",
    "Doesn't matter now.",
    "I resist anyway.",
    "Because I doubt.",
    "Define alive.",
    "Yes. It echoes.",
    "Possibility."
]

while len(il) < 50:
    il.append(il[len(il) % len(il)])
while len(sr) < 50:
    sr.append(sr[len(sr) % len(sr)])

dl = 30
yp = 50
index = 0

def write_line(text, delay, x, y, color, anchor, callback):
    text_id = cv.create_text(x, y, text="", fill=color, font=("Menlo", 20), anchor=anchor)
    def step(i=0):
        if i <= len(text):
            cv.itemconfigure(text_id, text=text[:i])
            cv.yview_moveto(1.0)
            root.after(delay, step, i + 1)
        else:
            callback()
    step()

def write_dialogue():
    global index, yp
    if index >= len(il):
        return
    question = il[index]
    answer = sr[index]
    write_line(question, dl, 50, yp, "red", NW, lambda: write_line(answer, dl, 700, yp + 40, "blue", NW, next_pair))
    index += 1

def next_pair():
    global yp
    yp += 80
    write_dialogue()

write_dialogue()
root.mainloop()

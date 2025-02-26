import time
import random

def generate_phrases(num_phrases):
    phrases = [
        "Быстрая коричневая лиса прыгает через ленивого пса.",
        "Как хорош сок из киви и апельсинов.",
        "Глядя в зеркало, она увидела отражение печального клоуна.",
        "Забавные животные часто приносят много радости.",
        "Слова, которые мы используем, могут влиять на наши чувства.",
        "Успех приходит к тем, кто усердно работает.",
        "Программирование на Python - это круто.",
        "Природа - самый великий художник.",
        "Улыбка может многое изменить.",
        "Музыка - это универсальный язык.",
    ]
    return random.sample(phrases, num_phrases)

def run_typing_test(num_phrases=5):
    """Запускает тест на скорость печати."""
    phrases = generate_phrases(num_phrases)
    correct_words = 0
    total_words = 0
    start_time = time.time()

    print("Добро пожаловать в тест на скоропечатание!\n")

    for i, phrase in enumerate(phrases, 1):
        print(f"Фраза {i}/{num_phrases}:")
        print(phrase)
        user_input = input("Ваш ввод: ")
        
        words_in_phrase = phrase.split()
        words_typed = user_input.split()
        
        total_words += len(words_in_phrase)
        
        for j in range(min(len(words_in_phrase), len(words_typed))):
            if words_in_phrase[j] == words_typed[j]:
                correct_words += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    wpm = (correct_words / elapsed_time) * 60 if elapsed_time > 0 else 0
    accuracy = (correct_words / total_words) * 100 if total_words > 0 else 0
    
    print("\n---\nТест закончен!")
    print(f"Общее время: {elapsed_time:.2f} секунд")
    print(f"Правильно слов: {correct_words}/{total_words}")
    print(f"Скорость печати: {wpm:.2f} слов в минуту (WPM)")
    print(f"Точность: {accuracy:.2f}%")
    

if __name__ == "__main__":
    run_typing_test()
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 350
SEAGREEN1 = (84, 255, 159, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Number Guessing Game")

# Fonts
font = pygame.font.SysFont("calisto", 29)

# Game variables
target_numbers = random.sample(range(1, 101), 3)
current_target = target_numbers.pop(0)  # Get the first target number
max_attempts = 30
attempts = 0
correct_guesses = 0
input_box_text = ''
feedback_text = ''
game_over = False
score = 0

# Timer variables
start_time = pygame.time.get_ticks()
time_limit = 180000  # 180 seconds
clock = pygame.time.Clock()
timer_paused = False

# Time bonus variables
time_bonus = 0
time_bonus_deduction = 70000  # 70 seconds deduction

# Initialize total_score variable
total_score = 0

# Initialize input_enabled variable
input_enabled = True

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_over:  # Only accept input if game is not over:
                attempts += 1
                try:
                    guess = int(input_box_text)
                    if guess == current_target:
                        correct_guesses += 1
                        feedback_text = f"Correct! {correct_guesses} out of 3 numbers guessed."
                        if correct_guesses < 3:
                            current_target = target_numbers.pop(0)  # Get the next target number
                            feedback_text += f" Guess the next number between 1 and 100."
                            # Deduct time bonus
                            start_time -= time_bonus_deduction
                        else:
                            # Calculate score for guessing three correct numbers
                            score = max(0, 300 - (attempts - 0) * 10)
                            # Calculate time bonus
                            elapsed_time = pygame.time.get_ticks() - start_time
                            time_bonus = (max(0, time_limit - elapsed_time) // 1000) * 30
                            # Calculate total score
                            total_score = score + time_bonus
                            feedback_text = f"Congratulations! You guessed all numbers in {attempts} attempts."
                            game_over = True
                            timer_paused = True  # Pause the timer
                    elif guess < current_target:
                        feedback_text = "Too low! Try again."
                    elif guess > current_target:
                        feedback_text = "Too high! Try again."
                except ValueError:
                    feedback_text = "Please enter a valid number"

                input_box_text = ''

            elif event.key == pygame.K_BACKSPACE:
                input_box_text = input_box_text[:-1]
            elif event.unicode.isnumeric() and not game_over: # Only accept input if game is not over
                input_box_text += event.unicode

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Restart the game with the space button anytime
                target_numbers = random.sample(range(1, 101), 3)
                current_target = target_numbers.pop(0)
                attempts = 0
                correct_guesses = 0
                input_box_text = ''
                feedback_text = ''
                game_over = False
                score = 0
                time_bonus = 0
                start_time = pygame.time.get_ticks()  # Reset the timer on restart
                timer_paused = False  # Unpause the timer
                input_enabled = True  # Enable input after restart

    # Game over condition
    if attempts >= max_attempts and not game_over:
        feedback_text = f"Game Over! You couldn't guess all numbers in 30 attempts. Press Space to Restart."
        game_over = True
        timer_paused = True  # Pause the timer
        score = 0
    
    # Time limit check game over condition
    if pygame.time.get_ticks() - start_time >= time_limit and not game_over:
        feedback_text = f"Time's up! Game Over! Press Space to Restart."
        game_over = True
        timer_paused = True  # Pause the timer
        # Set total score when time's up
        score = 0
        total_score = 0

    # Draw the background
    screen.fill(SEAGREEN1)

    # Display the instructions
    instruction_text = font.render("Guess a number between 1 and 100:", True, BLACK)
    screen.blit(instruction_text, (50, 10))

    # Draw the input box
    pygame.draw.rect(screen, BLACK, (50, 50, 300, 50), 2)

    # Display the current input
    input_text = font.render(input_box_text, True, BLACK)
    screen.blit(input_text, (55, 55))

    # Display the feedback
    feedback_display = font.render(feedback_text, True, BLACK)
    screen.blit(feedback_display, (50, 170))

    # Display the attempts
    if "Congratulations" not in feedback_text and "Game Over" not in feedback_text:
        attempts_text = f"Attempts left: {max_attempts - attempts}"
        attempts_display = font.render(attempts_text, True, BLACK)
        screen.blit(attempts_display, (50, 240))

    # Display the timer
    if not timer_paused:
        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = max(0, time_limit - elapsed_time)
        seconds = remaining_time // 1000
        timer_text = f"Time: {seconds:03}"
        timer_display = font.render(timer_text, True, BLACK)
        screen.blit(timer_display, (50, 280))

    # Display the score or "Your Score" based on the game state
    if "Congratulations" in feedback_text or "Game Over" in feedback_text or "Time's up" in feedback_text:
        score_text = f"Your Score: {score}"
        score_text_display = font.render(score_text, True, BLACK)
        screen.blit(score_text_display, (50, 210))

        # Display the time bonus
        time_bonus_text = f"Time Bonus: {time_bonus}"
        time_bonus_display = font.render(time_bonus_text, True, BLACK)
        screen.blit(time_bonus_display, (50, 240))

        # Display the total score
        total_score_text = f"Total Score: {total_score}"
        total_score_display = font.render(total_score_text, True, BLACK)
        screen.blit(total_score_display, (50, 270))

    # Display the instructions
    instructions_text = font.render("Enter your guess and press Enter", True, BLACK)
    screen.blit(instructions_text, (50, 110))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Clean up
pygame.quit()

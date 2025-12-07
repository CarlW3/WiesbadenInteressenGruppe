# Simon Says Game for Raspberry Pi Pico W
# Hardware Requirements:
# - 4 LEDs connected to GPIO pins (with resistors)
# - 4 Buttons connected to GPIO pins (with pull-down resistors)
# - I2C OLED Display (SSD1306 128x64)
# 
# Wiring:
# LEDs: GP0, GP1, GP2, GP3 (with 220Ω resistors to GND)
# Buttons: GP10, GP11, GP12, GP13 (pull-down, connect to 3.3V when pressed)
# I2C Display: SDA=GP14, SCL=GP15

from machine import Pin, I2C
import time
import random
from ssd1306 import SSD1306_I2C

class SimonSaysGame:
    """Simon Says memory game with LEDs, buttons and OLED display."""
    
    def __init__(self):
        # Configure LED pins
        self.leds = [
            Pin(0, Pin.OUT),   # LED 1 - Red
            Pin(1, Pin.OUT),   # LED 2 - Green
            Pin(2, Pin.OUT),   # LED 3 - Blue
            Pin(3, Pin.OUT)    # LED 4 - Yellow
        ]
        
        # Configure button pins with pull-down resistors
        self.buttons = [
            Pin(10, Pin.IN, Pin.PULL_DOWN),  # Button 1
            Pin(11, Pin.IN, Pin.PULL_DOWN),  # Button 2
            Pin(12, Pin.IN, Pin.PULL_DOWN),  # Button 3
            Pin(13, Pin.IN, Pin.PULL_DOWN)   # Button 4
        ]
        
        # Initialize I2C for OLED display
        self.i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
        self.display = SSD1306_I2C(128, 64, self.i2c)
        
        # Game state
        self.sequence = []
        self.score = 0
        self.game_over = False
        self.high_score = 0
        
        # LED colors for display (optional labels)
        self.led_names = ["RED", "GREEN", "BLUE", "YELLOW"]
        
        # Turn off all LEDs initially
        self.all_leds_off()
    
    def all_leds_off(self):
        """Turn off all LEDs."""
        for led in self.leds:
            led.value(0)
    
    def blink_led(self, led_index, duration=0.5):
        """Blink a specific LED."""
        self.leds[led_index].value(1)
        time.sleep(duration)
        self.leds[led_index].value(0)
        time.sleep(0.2)
    
    def flash_all_leds(self, times=3, duration=0.15):
        """Flash all LEDs simultaneously."""
        for _ in range(times):
            for led in self.leds:
                led.value(1)
            time.sleep(duration)
            self.all_leds_off()
            time.sleep(duration)
    
    def wait_for_button_press(self, timeout=5.0):
        """
        Wait for any button press and return the button index.
        Returns None if timeout occurs.
        """
        start_time = time.time()
        button_pressed = [False] * 4
        
        while (time.time() - start_time) < timeout:
            for i, button in enumerate(self.buttons):
                if button.value() == 1 and not button_pressed[i]:
                    # Button pressed - light up corresponding LED
                    self.leds[i].value(1)
                    time.sleep(0.1)
                    
                    # Wait for button release
                    while button.value() == 1:
                        time.sleep(0.01)
                    
                    self.leds[i].value(0)
                    time.sleep(0.1)
                    return i
            
            time.sleep(0.01)
        
        return None  # Timeout
    
    def display_message(self, line1="", line2="", line3="", line4="", clear=True):
        """Display text on OLED screen."""
        if clear:
            self.display.fill(0)
        
        if line1:
            self.display.text(line1, 0, 0)
        if line2:
            self.display.text(line2, 0, 16)
        if line3:
            self.display.text(line3, 0, 32)
        if line4:
            self.display.text(line4, 0, 48)
        
        self.display.show()
    
    def update_score_display(self):
        """Update the score on the display."""
        self.display_message(
            "SIMON SAYS",
            f"Score: {self.score}",
            f"High: {self.high_score}",
            "Watch & Repeat!"
        )
    
    def play_sequence(self):
        """Play the current LED sequence."""
        self.display_message("WATCH!", "", "Memorize the", "sequence...")
        time.sleep(1)
        
        for led_index in self.sequence:
            self.blink_led(led_index, duration=0.5)
    
    def get_player_input(self):
        """Get player's input sequence and verify it."""
        self.display_message("YOUR TURN!", "", "Repeat the", "sequence...")
        time.sleep(0.5)
        
        for step, correct_led in enumerate(self.sequence):
            # Wait for button press
            pressed_button = self.wait_for_button_press(timeout=5.0)
            
            if pressed_button is None:
                # Timeout
                self.display_message("TIMEOUT!", "", "Too slow!", "")
                time.sleep(1)
                return False
            
            if pressed_button != correct_led:
                # Wrong button
                self.display_message("WRONG!", "", f"Expected:", self.led_names[correct_led])
                self.flash_all_leds(times=5, duration=0.1)
                time.sleep(1)
                return False
        
        # Correct sequence!
        return True
    
    def add_to_sequence(self):
        """Add a random LED to the sequence."""
        new_led = random.randint(0, 3)
        self.sequence.append(new_led)
    
    def start_game(self):
        """Start a new game."""
        self.sequence = []
        self.score = 0
        self.game_over = False
        
        # Welcome screen
        self.display_message("SIMON SAYS", "", "Get Ready!", "")
        self.flash_all_leds(times=2)
        time.sleep(1)
        
        # Game loop
        while not self.game_over:
            # Add new LED to sequence
            self.add_to_sequence()
            
            # Show current score
            self.update_score_display()
            time.sleep(1.5)
            
            # Play the sequence
            self.play_sequence()
            
            # Get player input
            if self.get_player_input():
                # Correct! Increase score
                self.score += 1
                
                # Update high score
                if self.score > self.high_score:
                    self.high_score = self.score
                
                # Success feedback
                self.display_message("CORRECT!", "", f"Score: {self.score}", "Next round...")
                self.flash_all_leds(times=2, duration=0.1)
                time.sleep(1.5)
            else:
                # Game over
                self.game_over = True
                self.display_message("GAME OVER!", "", f"Final: {self.score}", f"Best: {self.high_score}")
                time.sleep(3)
                
                # Ask to play again
                self.display_message("Play Again?", "", "Press any", "button...")
                self.wait_for_button_press(timeout=10.0)
    
    def run(self):
        """Main game loop."""
        self.display_message("SIMON SAYS", "============", "Press button", "to start!")
        
        # Wait for initial button press
        self.wait_for_button_press(timeout=30.0)
        
        while True:
            try:
                self.start_game()
            except KeyboardInterrupt:
                self.display_message("BYE!", "", "Thanks for", "playing!")
                self.all_leds_off()
                time.sleep(2)
                break

# Main execution
if __name__ == "__main__":
    print("Starting Simon Says Game...")
    print("Hardware Setup:")
    print("  LEDs: GP0, GP1, GP2, GP3")
    print("  Buttons: GP10, GP11, GP12, GP13")
    print("  I2C Display: SDA=GP14, SCL=GP15")
    
    game = SimonSaysGame()
    game.run()

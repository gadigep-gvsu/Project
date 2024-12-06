from base_character import GameCharacter
import logging
import time

class Warrior(GameCharacter):
    def __init__(self, name):
        super().__init__(name, health=100, weapons=["Sword", "Shield"])
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def battle_cry(self):
        self.logger.info(f"{self.name} shouts: For glory!")
    
    def run(self):
        while True:
            self.logger.info("Warrior service is running...")
            time.sleep(30)

if __name__ == "__main__":
    warrior = Warrior("Aragorn")
    warrior.run()
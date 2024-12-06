from base_character import GameCharacter
import logging
import time

class Archer(GameCharacter):
    def __init__(self, name):
        super().__init__(name, health=80, weapons=["Bow", "Arrow Quiver"])
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def precise_shot(self):
        self.logger.info(f"{self.name} takes a precise aim!")
    
    def run(self):
        while True:
            self.logger.info("Archer service is running...")
            time.sleep(30)

if __name__ == "__main__":
    archer = Archer("Legolas")
    archer.run()
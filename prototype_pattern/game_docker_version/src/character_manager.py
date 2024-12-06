import logging
import time
from warrior import Warrior
from archer import Archer

class CharacterPrototypeManager:
    def __init__(self):
        self._prototypes = {}
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def register_prototype(self, name, prototype):
        self._prototypes[name] = prototype
        self.logger.info(f"Registered prototype: {name}")
    
    def clone_character(self, name, new_name=None):
        if name not in self._prototypes:
            raise ValueError(f"No prototype registered with name: {name}")
        
        cloned_character = self._prototypes[name].clone()
        
        if new_name:
            cloned_character.name = new_name
        else:
            base_name = cloned_character.__class__.__name__
            cloned_character.name = f"{base_name}_Clone_{id(cloned_character)}"
        
        self.logger.info(f"Cloned character: {cloned_character.name}")
        return cloned_character
    
    def run(self):
        # Create and register prototype characters
        warrior_prototype = Warrior("Aragorn")
        archer_prototype = Archer("Legolas")

        self.register_prototype("warrior", warrior_prototype)
        self.register_prototype("archer", archer_prototype)

        while True:
            self.logger.info("Character Manager service is running...")
            time.sleep(30)

if __name__ == "__main__":
    manager = CharacterPrototypeManager()
    manager.run()
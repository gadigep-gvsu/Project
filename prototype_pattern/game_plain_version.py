# Minimalist functional implementation of Prototype pattern
# real world scenario: design characters in a game
import copy

# Abstract base class for prototypical game characters
class GameCharacter:
    def __init__(self, name, health, weapons):
        self.name = name
        self.health = health
        self.weapons = weapons.copy()  # Ensure a deep copy of weapons list
    
    def clone(self):
        """
        Create a deep copy of the character using Python's copy module.
        This is the core of the Prototype pattern.
        """
        return copy.deepcopy(self)
    
    def take_damage(self, damage):
        """Reduce character health when hit"""
        self.health -= damage
    
    def display_info(self):
        """Show character details"""
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print("Weapons: " + ", ".join(self.weapons))
        print("---")

# Concrete character prototypes
class Warrior(GameCharacter):
    def __init__(self, name):
        super().__init__(name, health=100, weapons=["Sword", "Shield"])
    
    def battle_cry(self):
        print(f"{self.name} shouts: For glory!")

class Archer(GameCharacter):
    def __init__(self, name):
        super().__init__(name, health=80, weapons=["Bow", "Arrow Quiver"])
    
    def precise_shot(self):
        print(f"{self.name} takes a precise aim!")

# Prototype Manager to handle character creation and cloning
class CharacterPrototypeManager:
    def __init__(self):
        self._prototypes = {}
    
    def register_prototype(self, name, prototype):
        """Register a prototype character"""
        self._prototypes[name] = prototype
    
    def unregister_prototype(self, name):
        """Remove a prototype from the registry"""
        del self._prototypes[name]
    
    def clone_character(self, name, new_name=None):
        """
        Clone a registered prototype and optionally give it a new name.
        If no new name is provided, generates a unique name.
        """
        if name not in self._prototypes:
            raise ValueError(f"No prototype registered with name: {name}")
        
        cloned_character = self._prototypes[name].clone()
        
        if new_name:
            cloned_character.name = new_name
        else:
            # Generate a unique name if not provided
            base_name = cloned_character.__class__.__name__
            cloned_character.name = f"{base_name}_Clone_{id(cloned_character)}"
        
        return cloned_character

# Demonstration of the Prototype pattern
def main():
    # Create prototype manager
    prototype_manager = CharacterPrototypeManager()

    # Create and register prototype characters
    warrior_prototype = Warrior("Aragorn")
    archer_prototype = Archer("Legolas")

    prototype_manager.register_prototype("warrior", warrior_prototype)
    prototype_manager.register_prototype("archer", archer_prototype)

    # Demonstrate cloning
    print("Original Characters:")
    warrior_prototype.display_info()
    archer_prototype.display_info()

    # Clone characters
    warrior_clone1 = prototype_manager.clone_character("warrior")
    warrior_clone2 = prototype_manager.clone_character("warrior", "Boromir")
    archer_clone = prototype_manager.clone_character("archer")

    print("\nCloned Characters:")
    warrior_clone1.display_info()
    warrior_clone2.display_info()
    archer_clone.display_info()

    # Demonstrate independent modifications
    warrior_clone1.take_damage(30)
    warrior_clone1.weapons.append("Dagger")

    print("\nModified Cloned Warrior:")
    warrior_clone1.display_info()

    # Original remains unchanged
    print("Original Warrior (remains unchanged):")
    warrior_prototype.display_info()

if __name__ == "__main__":
    main()

# Execute the main function
main()
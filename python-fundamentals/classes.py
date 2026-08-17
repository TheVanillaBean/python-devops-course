# %% [markdown]
# # Classes and Objects
# - **Beyond Built-ins:** Python lets you define your own data types using `class`.
# - **Class:** A blueprint or template for creating objects. Defines attributes (data) and methods (behavior). Convention: `PascalCase` names (`MyClass`).
# - **Object (Instance):** A specific item created from a class blueprint. Each object has its own set of attribute values but shares the methods defined by the class. `obj1 = MyClass()`, `obj2 = MyClass()`. `obj1` and `obj2` are distinct objects.
# %% [markdown]
# ## Defining a Class & `__init__` (The Constructor)
# - **`__init__(self, ...)`:** Special method for initialization. `self` is always the first parameter and represents the instance itself. Other parameters receive arguments passed during object creation.
# - **Instance Attributes (`self.x = ...`):** Data attached to *this specific object*. Created inside methods (usually `__init__`) using `self.attribute_name = value`.
# %%
class ServiceMonitor:
    """Provides service checks for a single service"""
    def __init__(self, service_name, port):
        """Initializes the monitor for a specific service.

        Args:
            service_name (str): the name of the service.
            port (int): the port to use for checks.
        """
        print(f"Initializing monitor for service {service_name} on port {port}.")
        self.service = service_name
        self.port = port
        self.is_alive = False
# %% [markdown]
# ## Creating Instances (Objects)
# - **Mechanism:** Call the class name as if it were a function, passing any arguments required by `__init__` (after `self`).
# - Python automatically creates the object and passes it as `self` to `__init__`.
# %%
nginx_monitor = ServiceMonitor("nginx", 80)
print(isinstance(nginx_monitor, ServiceMonitor))

redis_monitor = ServiceMonitor(service_name="redis", port=6379)
print(isinstance(redis_monitor, ServiceMonitor))

print(nginx_monitor.service)
print(redis_monitor.service)
# %% [markdown]
# ## Instance Methods: Object Behavior
# - **Definition:** Functions defined *inside* a class definition.
# - **First Parameter:** Always `self` (by strong convention), allowing the method to access and modify the instance's attributes (`self.attribute_name`).
# - **Calling:** Use dot notation on an instance: `instance.method_name(arguments)`. Python automatically passes the instance (`instance`) as the `self` argument.
# %%
class ServiceMonitor:
    """Provides service checks for a single service"""
    def __init__(self, service_name, port):
        """Initializes the monitor for a specific service.

        Args:
            service_name (str): the name of the service.
            port (int): the port to use for checks.
        """
        print(f"Initializing monitor for service {service_name} on port {port}.")
        self.service = service_name
        self.port = port
        self.is_alive = False

    def check(self):
        """Simulates checking the service status"""
        print(f"METHOD: Checking {self.service} on port {self.port}...")
        self.is_alive = True
        print(f"METHOD: Status for service {self.service}: {"Alive" if self.is_alive else "Down"}")
        return self.is_alive

print(ServiceMonitor.check)
nginx_monitor = ServiceMonitor("nginx", 80)
status = nginx_monitor.check()
print(f"Received status: {status}")
# %% [markdown]
# ## Basic Inheritance: Reusing and Extending
# - **Concept:** Create a new class (Child/Subclass) that inherits properties (attributes and methods) from an existing class (Parent/Superclass). Promotes code reuse (DRY).
# - **Syntax:** `class ChildClassName(ParentClassName):`
# - **Inherited Members:** The Child automatically gets all methods and attributes defined in the Parent.
# - **Specializing:** The Child can:
#   - Add *new* attributes and methods.
#   - *Override* parent methods by defining a method with the same name.
# - **`super()`:** Inside the Child's methods, use `super().method_name(...)` to explicitly call the Parent's version of a method (very common in `__init__`).
# %%
class HttpServiceMonitor(ServiceMonitor):
    """Extends ServiceMonitor to add an HTTP endpoint check."""
    def __init__(self, service_name, port, url):
        super().__init__(service_name, port)
        self.url = url

    def ping(self):
        """Ping url provided when creating instance."""
        print(f"METHOD: Pinging url {self.url}")

    def check(self):
        alive = super().check()
        print(f"METHOD: Performing HTTP check on {self.url}")

http_monitor = HttpServiceMonitor("web", 8080, "http://localhost")
nginx_monitor = ServiceMonitor("nginx", 80)

http_monitor.ping()
http_monitor.check()
# nginx_monitor.ping() # Uncommenting will raise AttributeError since ping() is a method only of the subclass
nginx_monitor.check()
# %%
import types
class Room:
    def __init__(self, number_of_beds):
        self.number_of_beds = number_of_beds

class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs) + 1

    # Add this method to handle class methods properly
    def __get__(self, instance, owner):
        if instance is None:
            return self
        # Dynamically binds the 'hotel' instance to the function
        return types.MethodType(self, instance)

# def logger(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs) + 1
#     return wrapper

class Hotel:
    def __init__(self, rooms):
        self.rooms = rooms

    @Logger
    def number_of_rooms(self):
        return len(self.rooms)

one_bed = Room(1)
two_bed = Room(2)

hotel = Hotel([one_bed, two_bed])

print(hotel.number_of_rooms())
# %%
def gen_numbers(end):
    for i in range(0, end):
        yield i


gen_10_numbers = gen_numbers(10)

print(next(gen_10_numbers))
print(next(gen_10_numbers))

for num in gen_10_numbers:
    print(num)

# print(next(gen_10_numbers)) ##raises StopIteration exception

print("\n")

gen_15_numbers = (num for num in range(0, 15))

for num in gen_15_numbers:
    print(num)



# %%
EXAMPLE_INTERSECTION = {'fresh red chili', 'sugar', 'nutritional yeast', 'fresh ginger', 'red chili powder', 'garlic',
                        'olive oil', 'mashed potatoes', 'garam masala', 'clove powder', 'cumin powder', 'onion',
                        'chickpea flour', 'water', 'turmeric powder', 'hing', 'black pepper', 'cinnamon powder',
                        'cilantro', 'salt', 'oil', 'cardamom powder', 'turmeric', 'garlic paste', 'mustard seeds',
                        'vinegar', 'mangoes', 'nigella seeds', 'serrano chili', 'flour', 'soy sauce', 'coriander seeds',
                        'coriander powder', 'lemon juice', 'mango powder', 'curry leaves'}

example_dishes = [
                  {'salt', 'breadcrumbs', 'water', 'flour', 'celeriac', 'chickpea flour', 'soy sauce', 'parsley',
                   'sunflower oil', 'lemon', 'black pepper'},

                  {'cornstarch', 'salt', 'vegetable oil', 'sugar', 'vegetable stock', 'water', 'tofu', 'soy sauce',
                   'lemon zest', 'lemon juice', 'black pepper', 'ginger', 'garlic'},

                  {'salt', 'mixed herbs', 'silken tofu', 'smoked tofu', 'nutritional yeast', 'turmeric', 'soy sauce',
                   'garlic', 'lemon juice', 'olive oil', 'black pepper', 'spaghetti'},

                  {'salt', 'mushrooms', 'sugar', 'barley malt', 'nutritional yeast', 'fresh basil', 'olive oil',
                   'honey', 'yeast', 'red onion', 'bell pepper', 'cashews', 'oregano', 'rosemary', 'garlic powder',
                   'tomatoes', 'water', 'flour', 'red pepper flakes', 'garlic'},

                  {'mango powder', 'oil', 'salt', 'cardamom powder', 'fresh red chili', 'sugar', 'fresh ginger',
                   'turmeric', 'red chili powder', 'curry leaves', 'garlic paste', 'mustard seeds', 'vinegar',
                   'mashed potatoes', 'garam masala', 'mangoes', 'nigella seeds', 'clove powder', 'serrano chili',
                   'cumin powder', 'onion', 'water', 'chickpea flour', 'coriander seeds', 'turmeric powder', 'hing',
                   'coriander powder', 'cinnamon powder', 'cilantro', 'garlic'},

                  {'mango powder', 'oil', 'salt', 'cardamom powder', 'fresh red chili', 'sugar', 'fresh ginger',
                   'turmeric', 'red chili powder', 'curry leaves', 'garlic paste', 'mustard seeds', 'vinegar',
                   'mashed potatoes', 'garam masala', 'mangoes', 'nigella seeds', 'clove powder', 'serrano chili',
                   'cumin powder', 'onion', 'water', 'chickpea flour', 'coriander seeds', 'turmeric powder', 'hing',
                   'coriander powder', 'cinnamon powder', 'cilantro', 'garlic'}
                  ]

for dish in example_dishes:
    intersection = dish.intersection(EXAMPLE_INTERSECTION)
    union = dish.union(EXAMPLE_INTERSECTION)
    difference = dish.difference(EXAMPLE_INTERSECTION)
    ym = dish.symmetric_difference(EXAMPLE_INTERSECTION)
    print(intersection)
# %%

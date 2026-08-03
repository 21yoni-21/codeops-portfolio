#exercise 1.................................



class Report:
    def build(self):
        return "Report content"


class ReportSaver:
    def save(self, report):
        print(f"Saving: {report}")


class ReportEmailer:
    def send(self, report):
        print(f"Emailing: {report}")


report = Report()

content = report.build()

saver = ReportSaver()
emailer = ReportEmailer()

saver.save(content)
emailer.send(content)

#exercise   .......................


class Shape:

    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


shapes = [
    Circle(5),
    Square(4)
]


for shape in shapes:
    print(shape.area())

#exercise...................................




class AppSettings:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"

        return cls._instance


app1 = AppSettings()
app2 = AppSettings()


print(app1.currency)
print(app1 is app2)


#exercise.......................................




class Triangle:

    def area(self):
        return "Triangle area"


class ShapeFactory:

    @staticmethod
    def create(kind):

        if kind == "circle":
            return Circle(3)

        elif kind == "square":
            return Square(5)

        elif kind == "triangle":
            return Triangle()

        else:
            raise ValueError("Unknown shape")


shape1 = ShapeFactory.create("circle")
shape2 = ShapeFactory.create("triangle")


print(shape1.area())
print(shape2.area())

#exercise.................................



class NewsAgency:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)


    def notify(self, news):

        for subscriber in self.subscribers:
            subscriber.update(news)



class EmailSubscriber:

    def update(self, news):
        print(f"Email received: {news}")



class SMSSubscriber:

    def update(self, news):
        print(f"SMS received: {news}")



agency = NewsAgency()

email = EmailSubscriber()
sms = SMSSubscriber()


agency.subscribe(email)
agency.subscribe(sms)


agency.notify("New Python course available")


#added

from bank import *


sms = SMSAlert()
audit = AuditLog()


saving = AccountFactory.create(
    "savings",
    "Yonas",
    "001",
    1000
)

current = AccountFactory.create(
    "current",
    "Abel",
    "002",
    500
)


saving.subscribe(sms)
saving.subscribe(audit)

current.subscribe(sms)
current.subscribe(audit)


saving.deposit(500)
saving.add_interest()

current.withdraw(900)


accounts = [
    saving,
    current
]

for account in accounts:
    print(account.statement())
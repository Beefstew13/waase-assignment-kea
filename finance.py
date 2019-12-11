from datetime import datetime


class Finance:

    def __init__(self):
        self.reports = []

    def create_report(self, cart):
        total_price = 0
        report = ''
        for bike, amount in cart:
            item_price = bike.price*amount
            total_price += item_price
            report += f'{bike.model}            {amount}x${bike.price} =  ${item_price}\n'
        report += f'Date = { datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}'
        report += f'Total price = ${total_price}'
        self.reports.append(report)
        return report

    def display_reports(self):
        for report in self.reports:
            print(report)

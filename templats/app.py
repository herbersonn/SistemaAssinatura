from decimal import Decimal
import __init__
from models.model import Subscription, Payments
from views.view import SubscriptionService
from models.database import engine
from datetime import date, datetime


class UI:
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)


    def add_subscription(self):
        empresa = input('Empresa: ')
        site = input('Site: ')
        data_assinatura = datetime.strptime(input('Data de assinatura: '), '%d/%m/%Y')
        valor = Decimal(input('Valor: '))

        
        subscription = Subscription(empresa=empresa, site=site, data_assinatura=data_assinatura, valor=valor)
        self.subscription_service.create(subscription)
        print('Assinatura adicionada com sucesso.')



    def delete_subscription(self):
        subscriptions = self.subscription_service.list_all()
        print('Escolha qual assinatura deseja excluir')


        for i in subscriptions:
            print(f'[{i.id}] -> {i.empresa}')

        choice = int(input('Escolha a assinatura: '))
        self.subscription_service.delete(choice)
        print('Assinatura excluída com sucesso.')


    def total_value(self):
        print(f'Seu valor total mensal em assinaturas: {self.subscription_service.total_value()}')



    def start(self):
            while True:
                print('''
                [1] -> Adicionar assinatura
                [2] -> Remover assinatura
                [3] -> Valor total
                [4] -> Gastos últimos 12 meses
                [5] -> Sair
                ''')
                choice = int(input('Escolha uma opção: '))
                if choice == 1:
                    self.add_subscription()
                elif choice == 2:
                    self.delete_subscription()
                elif choice == 3:
                    self.total_value()
                elif choice == 4:
                    self.subscription_service.gen_chart()
                else:
                    break




if __name__ == '__main__':
    UI().start()
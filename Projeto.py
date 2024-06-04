# Importar bibliotecas necessárias
import datetime

# Classe Veiculo
class Veiculo:
    def __init__(self, modelo, marca, ano, placa, vin):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.placa = placa
        self.vin = vin
        self.manutencao = []
        self.abastecimentos = []
        self.motoristas = []

    def registrar_manutencao(self, data, servico, quilometragem, custo):
        self.manutencao.append({"data": data, "servico": servico, "quilometragem": quilometragem, "custo": custo})

    def registrar_abastecimento(self, data, quantidade, custo):
        self.abastecimentos.append({"data": data, "quantidade": quantidade, "custo": custo})

    def adicionar_motorista(self, motorista):
        self.motoristas.append(motorista)

# Classe Motorista
class Motorista:
    def __init__(self, nome, licenca):
        self.nome = nome
        self.licenca = licenca

# Classe GestaoFrota
class GestaoFrota:
    def __init__(self):
        self.veiculos = []

    def cadastrar_veiculo(self):
        modelo = input("Informe o modelo do veículo: ")
        marca = input("Informe a marca do veículo: ")
        ano = int(input("Informe o ano do veículo: "))
        placa = input("Informe a placa do veículo: ")
        vin = input("Informe o VIN do veículo: ")
        veiculo = Veiculo(modelo, marca, ano, placa, vin)
        self.veiculos.append(veiculo)
        print("Veículo cadastrado com sucesso!")

    def registrar_manutencao(self):
        placa = input("Informe a placa do veículo: ")
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                data = datetime.date.today()
                servico = input("Informe o serviço realizado: ")
                quilometragem = float(input("Informe a quilometragem do veículo: "))
                custo = float(input("Informe o custo do serviço: "))
                veiculo.registrar_manutencao(data, servico, quilometragem, custo)
                print("Manutenção registrada com sucesso!")
                return
        print("Veículo não encontrado!")

    def registrar_abastecimento(self):
        placa = input("Informe a placa do veículo: ")
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                data = datetime.date.today()
                quantidade = float(input("Informe a quantidade de combustível abastecida: "))
                custo = float(input("Informe o custo do abastecimento: "))
                veiculo.registrar_abastecimento(data, quantidade, custo)
                print("Abastecimento registrado com sucesso!")
                return
        print("Veículo não encontrado!")

    def adicionar_motorista(self):
        placa = input("Informe a placa do veículo: ")
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                nome = input("Informe o nome do motorista: ")
                licenca = input("Informe a licença do motorista: ")
                motorista = Motorista(nome, licenca)
                veiculo.adicionar_motorista(motorista)
                print("Motorista adicionado com sucesso!")
                return
        print("Veículo não encontrado!")

    def gerar_relatorio(self):
        print("Relatório de Frota:")
        for veiculo in self.veiculos:
            print(f"Veículo: {veiculo.modelo} - {veiculo.placa}")
            print(f"Manutenções: {len(veiculo.manutencao)}")
            print(f"Abastecimentos: {len(veiculo.abastecimentos)}")
            print(f"Motoristas: {len(veiculo.motoristas)}")
            print("")

# Criar instância da classe GestaoFrota
gestao_frota = GestaoFrota()

# Menu de opções
while True:
    try:
        print("==============================")
        print("Menu de Opções: \n")
        print("1. Cadastrar Veículo")
        print("==============================")
        print("2. Registrar Manutenção")
        print("==============================")
        print("3. Registrar Abastecimento")
        print("==============================")
        print("4. Adicionar Motorista")
        print("==============================")
        print("5. Gerar Relatório")
        print("==============================")
        print("6. Sair")
        print("==============================")
        opcao = int(input("Escolha uma ação: "))

        if opcao == 1:
            gestao_frota.cadastrar_veiculo()
        elif opcao == 2:
            gestao_frota.registrar_manutencao()
        elif opcao == 3:
            gestao_frota.registrar_abastecimento()
        elif opcao == 4:
            gestao_frota.adicionar_motorista()
        elif opcao == 5:
            gestao_frota.gerar_relatorio()
        elif opcao == 6:
            print("Encerrando o programa...")
            break
    except ValueError:
        print("\nOpção inválida, tente novamente!\n")
'''

Exercícios 05
    Enunciado: Árvore Genealógica

    Imagine que você recebeu a tarefa de criar uma árvore genealógica para uma família.
    
    A árvore deve ser capaz de armazenar informações sobre várias gerações de uma família e suas relações.

    Requisitos:

        Modelo de Dados:

            Cada membro da família deve ser representado como um dicionário contendo: nome, idade, sexo e uma lista de filhos.
            
            A lista de filhos de cada membro da família deve conter dicionários representando cada filho.
            
            Funções a serem implementadas:

                adicionar_membro(nome, idade, sexo, pai=None):
                    
                    Adiciona um membro à árvore genealógica.
                    
                    Se o pai for especificado, o membro é adicionado como filho desse pai.
                    
                buscar_membro(nome):

                    Retorna o dicionário representando o membro da família com o nome especificado. 
                
                descendentes(nome):
                    
                    Retorna uma lista de todos os descendentes do membro com o nome especificado.
                    
                    Esta função deve ser implementada de forma recursiva. 
            
            Exemplo de Uso:

                Adicione um membro chamado "João" com 70 anos.
                
                Adicione um filho para "João" chamado "Carlos" com 50 anos.
                
                Adicione um filho para "Carlos" chamado "Pedro" com 30 anos.
                
                Adicione um filho para "Pedro" chamado "Lucas" com 10 anos.
                
                Ao chamar a função descendentes("João"), ela deve retornar uma lista contendo "Carlos", "Pedro" e "Lucas".
                
        Desafio Extra:

        Implemente uma função antepassados(nome) que, dado o nome de um membro, retorna uma lista de todos os seus antepassados diretos (pai, avô, bisavô, etc.).
        
        Esta função também deve ser implementada de forma recursiva.
        
        Este enunciado exige que o aluno utilize listas para armazenar os filhos de cada membro, dicionários para armazenar informações sobre cada membro e recursividade para buscar descendentes e antepassados.
'''

class ArvoreGenealogica:
    def __init__(self):
        self.membros = []

    def adicionar_membro(self, nome, idade, sexo, pai=None):
        #criar dicionário novo membro
        novo_membro = {'nome': nome, 'idade': idade, 'sexo': sexo, 'filhos': [], 'pai': pai}
        
        # se um pai for especificado, adicionar o novo membro como filho
        if pai:
            pai_encontrado = self.buscar_membro(pai)
            if pai_encontrado:
                pai_encontrado['filhos'].append(novo_membro)
        
        # adicionar membro à lista de membros da árvore
        self.membros.append(novo_membro)

    def buscar_membro(self, nome):
        # buscar membro pelo nome
        for membro in self.membros:
            if membro['nome'] == nome:
                return membro
        return None

    def descendentes(self, nome):
        # buscar o membro
        membro = self.buscar_membro(nome)
        if membro:
            # lista armazenar os descendentes
            lista_descendentes = []
            # adicionar filhos diretamente
            for filho in membro['filhos']:
                lista_descendentes.append(filho['nome'])
                # recursivamente adicionar descendentes dos filhos
                lista_descendentes.extend(self.descendentes(filho['nome']))
            return lista_descendentes
        return []

    def antepassados(self, nome):
        # buscar o membro
        membro = self.buscar_membro(nome)
        if membro:
            lista_antepassados = []
            # verificar membro tem pai
            if membro['pai']:
                pai = self.buscar_membro(membro['pai'])
                if pai:
                    # determinar grau de parentesco
                    lista_antepassados.append(f"Pai: {pai['nome']}")
                    # recursivamente adicionar os antepassados do pai
                    lista_antepassados.extend(self.antepassados_paterno(pai['nome'], "Avô"))
            return lista_antepassados
        return []

    def antepassados_paterno(self, nome, grau):
        # bscar o membro
        membro = self.buscar_membro(nome)
        if membro:
            lista_antepassados = []
            # se houver pai, adicionar o nome do pai com a relação
            if membro['pai']:
                pai = self.buscar_membro(membro['pai'])
                if pai:
                    lista_antepassados.append(f"{grau}: {pai['nome']}")
                    # recursivamente adicionar antepassados do pai
                    lista_antepassados.extend(self.antepassados_paterno(pai['nome'], "Bisavô"))
            return lista_antepassados
        return []

# criando a AG
arvore = ArvoreGenealogica()

# sdicionando membros
arvore.adicionar_membro("João", 70, "Masculino")
arvore.adicionar_membro("Carlos", 50, "Masculino", pai="João")
arvore.adicionar_membro("Pedro", 30, "Masculino", pai="Carlos")
arvore.adicionar_membro("Lucas", 10, "Masculino", pai="Pedro")

# tstando a função descendentes
print(arvore.descendentes("João"))  # Esperado: ['Carlos', 'Pedro', 'Lucas']

# testando a função antepassados
print(arvore.antepassados("Lucas"))  # Esperado: ['Pai: Pedro', 'Avô: Carlos', 'Bisavô: João']

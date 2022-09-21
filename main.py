from validate_docbr import CNPJ
from cpf_cnpj import Documento

exemplo_cnpj = "35379838000112"
exemplo_cpf = "53327004072"


documento = Documento.cria_documento(exemplo_cnpj)
print(documento)
documento2 = Documento.cria_documento(exemplo_cpf)
print(documento2)
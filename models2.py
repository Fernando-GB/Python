 from models import Perfil
 perfis = Perfil.gerar_perfis('perfis.csv')
 for p in perfis:
         p.imprimir()
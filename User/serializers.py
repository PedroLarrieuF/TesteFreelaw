from rest_framework import serializers
from .models import Usuario
import hashlib
import os

def make_password(password, salt=None, hash_algorithm='sha1'):
    """
    Criptografa uma senha usando um algoritmo de hash especificado.

    Argumentos:
    password (str): A senha a ser criptografada.
    salt (str, opcional): Um valor aleatório usado para salgar a senha. Se não for fornecido, um será gerado automaticamente.
    hash_algorithm (str, opcional): O algoritmo de hash a ser usado. Pode ser 'md5', 'sha1' ou 'sha256'. O padrão é 'sha1'.

    Retorna:
    str: A senha criptografada no formato "{algoritmo}${salt}${hash}".
    """
    if not salt:
        salt = os.urandom(8).hex()
    hash_obj = hashlib.new(hash_algorithm)
    hash_obj.update((salt + password).encode('utf-8'))
    return "%s$%s$%s" % (hash_algorithm, salt, hash_obj.hexdigest())

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'cpf', 'email', 'senha', 'regiao_brasil']
        extra_kwargs = {
            'senha': {'write_only': True}
        }

    def create(self, validated_data):
        # Antes de criar o usuário, criptografa a senha
        validated_data['senha'] = make_password(validated_data['senha'])
        return super().create(validated_data)

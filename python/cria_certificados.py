#!/opt/anaconda3/bin/python3

## Importando modulos:
import os, sys, socket

### Variaveis:
path = "/tmp/teste"
host = socket.gethostname()
OU = 'SPC'
L = 'Sao Paulo'
ST = 'Sao Paulo'
C = 'BR'
senha = "#spclab@"
validade = 365
chave_jks ='{path}/{host}.jks'.format(path=path,host=host)
chave_cer ='{path}/{host}.cer'.format(path=path,host=host)
chave_p12 ='{path}/{host}.p12'.format(path=path,host=host)
local_pem ='{path}/{host}.pem'.format(path=path,host=host)
dname='CN={host},OU={OU},L={L},ST={ST},C={C}'.format(host=host,OU=OU,L=L,ST=ST,C=C)
jks = 'keytool -genkeypair -keystore {chave_jks} -keyalg RSA -alias {host} -dname "{dname}" -storepass \'{senha}\' -keypass \'{senha}\' -validity {validade}'.format(chave_jks=chave_jks,host=host,dname=dname,senha=senha,validade=validade)
cer = 'keytool -export -alias {host} -keystore {chave_jks} -rfc -file {chave_cer} -storepass \'{senha}\''.format(host=host,chave_jks=chave_jks,chave_cer=chave_cer,senha=senha)
p12 = 'keytool -importkeystore -srckeystore {chave_jks} -srcstorepass \'{senha}\' -srckeypass \'{senha}\' -destkeystore {chave_p12} -deststoretype PKCS12 -srcalias {host} -deststorepass \'{senha}\' -destkeypass \'{senha}\''.format(chave_jks=chave_jks,senha=senha,chave_p12=chave_p12,host=host)
pem = 'openssl pkcs12 -in {chave_p12} -passin pass:{senha} -out {local_pem} -passout pass:{senha}'.format(chave_p12=chave_p12,senha=senha,local_pem=local_pem)
l_agent_jks = 'ln -sf {chave_jks} {path}/agent.jks'.format(chave_jks=chave_jks,path=path)
l_agent_pem = 'ln -sf {local_pem} {path}/agent.pem'.format(local_pem=local_pem,path=path)
agent_jks = '{path}/agent.jks'.format(path=path)
agent_pem = '{path}/agent.pem'.format(path=path)

### 1 - Criando diretórios
if not os.path.exists(path):
  try:
    os.makedirs(path,exist_ok=True)
  except:
    raise OSError('Deu ruim!')
else:
  print('Diretório ' + path + ' já existe!')

if os.path.exists(path):
  print('Passo 1: Criação dos diretórios OK!')

### 2 - Criando a chave JKS:
if not os.path.exists(chave_jks):
  try:
    os.system(jks)
  except:
    raise OSError('Deu ruim!')
else:
  print('A chave JKS ' + chave_jks + ' já existe!')

if os.path.exists(chave_jks):
  print('Passo 2: Criação da chave JKS OK!')

## 3 - Gerando o certificado .cer com base no .jks:
if not os.path.exists(chave_cer):
  try:
    os.system(cer)
  except:
    raise OSError('Deu ruim!')
else:
  print('O certificado ' + chave_cer + ' já existe!')

if os.path.exists(chave_cer):
  print('Passo 3: Criação do .cer a partir do .jks OK!')

## 4 - Gerando o certificado .p12 com base no .jks:
if not os.path.exists(chave_p12):
  try:
    os.system(p12)
  except:
    raise OSError('Deu ruim!')
else:
  print('O certificado ' + chave_p12 + ' já existe!')

if os.path.exists(chave_p12):
  print('Passo 4: Criação do certificado .p12 com base no .jks OK!')

## 5 - Gerando o certificado .pem com base no .p12:
if not os.path.exists(local_pem):
  try:
    os.system(pem)
  except:
    raise OSError('Deu ruim!')
else:
  print('O certificado ' + local_pem + ' já existe!')

if os.path.exists(local_pem):
  print('Passo 5: Criação do certificado .pem com base no .p12 OK!')

## 6 - Criando os links simbolicos:
if not os.path.exists(agent_jks):
  try:
    os.system(l_agent_jks)
  except:
    raise OSError('Deu ruim!')
else:
  print('O certificado ' + l_agent_jks + ' já existe!')

if not os.path.exists(agent_pem):
  try:
    os.system(l_agent_pem)
  except:
    raise OSError('Deu ruim!')
else:
  print('O certificado ' + l_agent_pem + ' já existe!')

if os.path.exists(agent_pem) and os.path.exists(agent_jks):
  print('Passo 6: Criação dos links simbólicos dos agents OK!')


### Finalizando:
print(' ')
print('Script concluído!')
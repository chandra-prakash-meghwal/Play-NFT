# Play-NFT

## prerequisites
pip install -r requirements.txt

## deploy NFTs
```
from scripts.deployment import main as deploy_main
deploy_main(owner_address='ownder wallet address', owner_private_key='owner private key', network='network e.g. ropsten')
```

## deploy Referee Contract
```
from scripts.deployment_referee import main as deploy_referee
deploy_referee(owner_address='ownder wallet address', owner_private_key='owner private key', network='network e.g. ropsten')
```

## create teams
```
from scripts.deployment_referee import create_teams
create_teams()
```

## get winner
```
from scripts.deployment_referee import get_winner
get_winner()
```

# update health daily
```
from scripts.contract_interaction import main as interact_main
interact_main(owner_address='ownder wallet address', owner_private_key='owner private key', network='network e.g. ropsten')
```

## NFTs deployed on ropsten
1. {'name': 'CIS', 'symbol': 'CIS-Play', 'detail': 'CISCO Systems (Nasdaq - US)'} 

    Ropsten Contract deployed to 0x4Fef796703eE7b96bcfDed3A305c54D1b420a2e9

2. {'name': 'TCS', 'symbol': 'TCS-Play', 'detail': 'Tata Consultancy (NSE - India)'}

    Ropsten! Contract deployed to 0x660EbB492b247AA454933e0f459EEc90d2ADA62D

3. {'name': 'RIL', 'symbol': 'RIL-Play', 'detail': 'Reliance Industries (NSE - India)'}

   Ropsten! Contract deployed to 0xD4251fD84cED3F78a923429c105dcd45fA50b099

4. {'name': 'SOC', 'symbol': 'SOC-Play', 'detail': 'Saudi Arabian Oil Company (Saudi - Saudia Arabia)'}

   Ropsten! Contract deployed to 0xaf2397F8cf84F4ebEBbC8b01eaAbc167AF369972

5. {'name': 'CWP', 'symbol': 'CWP-Play', 'detail': 'China Western Power Industrial Co., Ltd. (Shenzen - China)'}

    Ropsten! Contract deployed to 0x3F611196B7c31962D671170A2fE0476444bf4eA8

6. {'name': 'BBS', 'symbol': 'BBS-Play', 'detail': 'Banco do Brasil S.A. (Sao Paulo - Brazil)'}

    Ropsten! Contract deployed to 0x347A3729FbCFF2888f4d86D6af453826aE82D9e0

7. {'name': 'BBP', 'symbol': 'BBP-Play', 'detail': 'Balfour Beatty plc (LSE - UK)'}

    Ropsten! Contract deployed to 0x8C7C37048Da2Aeb0bF7a963eb282730F2FE83494

8. {'name': 'ZMT', 'symbol': 'ZMT-Play', 'detail': 'Zomato (NSE - India)'}

    Ropsten! Contract deployed to 0x7774440594b04363563ac2aEF4CDBaE6Ecb17802

9. {'name': 'JZH', 'symbol': 'JZH-Play', 'detail': 'Jiangsu Zhongchao Holding Co., Ltd. (Shenzen - China)'}

    Ropsten! Contract deployed to 0x80fEE58E6EaC4173B994f5EC61Cda13aB7f63533

10. {'name': 'TMC', 'symbol': 'TMC-Play', 'detail': 'Toyota Motor Corporation (Tokyo - Japan)'}

    Ropsten! Contract deployed to 0x0B28DF3E1e72CFcA3d822DB28A439f2911987531


## Referee Contract deployed on ropsten
0xbAFc9Dd88Ed6cf800895945bb421B5fdA167217F
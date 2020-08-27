# crypto-arbitrage

## Calculating spread on centralized (CEx) and decentrazlied exchanges (DEx)

### Centralized exchanges (ETH - USD)
Written in Python

    Binance
    Bitfinex
    Coinbase

### Decentralized exchanges (ETH - DAI)
Written in js, based on uniswap developer documentation

    Uniswap
    Balancer (coming soon)
    Curve (coming soon)

# Installing & Running
### Centralized module
1.  ``` bash
    pip install cbpro
    ```

2. Download and install the bitfinex API, using their instructions
    
    ```https://github.com/bitfinexcom/bitfinex-api-py```

3. Run
    ```
    python arbitrager.py
    ```
### Decentralized module
1. Make sure you have npm and nodejs installed (sudo apt install both)
2. Also need to have yarn installed (sudo apt install)
3. Get an Etherscan free API key (https://etherscan.io/apis)
4. Create a file called "keys.txt" in the /decentralized/ directory with your API key and the following content
    ```
    export ETHERSCAN_API_KEY="ETHERSCAN_API_KEY (keep the quotes)"
    ```
3. Run
    ```bash
    npm i
    npm run main
    ```

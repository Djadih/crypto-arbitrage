const UNISWAP_SDK = require("@uniswap/sdk");
const PROVIDERS = require("@ethersproject/providers");

const DAI = new UNISWAP_SDK.Token(
    UNISWAP_SDK.ChainId.MAINNET,
    "0x6B175474E89094C44Da98b954EedeAC495271d0F",
    18
);

const provider = new PROVIDERS.EtherscanProvider(
    "homestead",
    process.env.ETHERSCAN_API_KEY
  );

async function get_price() {
    // note that you may want/need to handle this async code differently,
    // for example if top-level await is not an option
    const pair = await UNISWAP_SDK.Fetcher.fetchPairData(
      DAI,
      UNISWAP_SDK.WETH[DAI.chainId],
      provider
    );
  
    const WETH_DAI = new UNISWAP_SDK.Route([pair], UNISWAP_SDK.WETH[DAI.chainId], DAI);
    const DAI_WETH = new UNISWAP_SDK.Route([pair], DAI, UNISWAP_SDK.WETH[DAI.chainId]);
  
    console.log("ETH -> DAI : " + WETH_DAI.midPrice.toSignificant(6));
    console.log("DAI -> ETH : " + DAI_WETH.midPrice.toSignificant(6));
}

exports.get_price = get_price
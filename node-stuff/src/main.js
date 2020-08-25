const UNISWAP = require("@uniswap/sdk");
const PROVIDERS = require("@ethersproject/providers");

const DAI = new UNISWAP.Token(
  UNISWAP.ChainId.MAINNET,
  "0x6B175474E89094C44Da98b954EedeAC495271d0F",
  18
);

const provider = new PROVIDERS.EtherscanProvider(
  "homestead",
  process.env.ETHERSCAN_API_KEY
);

async function f() {
  // note that you may want/need to handle this async code differently,
  // for example if top-level await is not an option
  const pair = await UNISWAP.Fetcher.fetchPairData(
    DAI,
    UNISWAP.WETH[DAI.chainId],
    provider
  );

  const route = new UNISWAP.Route([pair], UNISWAP.WETH[DAI.chainId]);

  console.log(route.midPrice.toSignificant(6));
  console.log(route.midPrice.invert().toSignificant(6));
}

f();
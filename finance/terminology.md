## The Greeks

1. Delta $\Delta$: Rate of change in options price per one unit change in the price of the underlying asset. Positive for call and negative for put. $\Delta = \frac{\partial V}{\partial S}$ where $V$ is the options price and $S$ is the price of the underlying asset.
2. Gamma $\Gamma$: Rate of change of delta per one unit change in the price of the underlying asset. Therefore always positive. $\Gamma = \frac{\partial^2 V}{\partial S^2} = \frac{\partial \Delta}{\partial S}$
3. Vega $\nu$: Sensitivity of options price to 1% change in implied volitility of underlying asset. At its maximum when the option price is at the money. $\nu = \frac{\partial\Nu}{\partial\sigma}$ where $\Nu$ is the price of the option and $\sigma$ is volatility.
4. Theta $\Theta$: Rate of change in options price per one-day decrease in time to expiry. Always negative. $\Theta = \frac{\partial V}{\partial T}$ where $V$ is the price of the option (call or put) and $t$ is the time to expiry.
5. Rho $\rho$: Sensitivty of options price to 1% change in intereset rates. $\rho = \frac{\partial V}{\partial r}$ where $V$ is the price of the option (call or put) and $r$ is the risk-free interest rate.

## Fixed Income Securities

### Bond

- A debt security under which the issuer owes the holders a debt and (depending on terms) must pay fixed or floating interest (coupon) and repay the princial at maturity date. Interest is payable at fixed intervals (annual, quarterly, etc.)
- Ownership can be transferred in secondary markets
- Low risk
- Issues by governments and corporations so they can raise money

### Cap/Floor (nonlinear)

- Types of interest rate derivatives used to hedge against interest rate fluctuations

#### Cap

- If interest rates rise *above* the strike(predefined level), seller compensates buyer for the differences (calculates using $\Delta$ and principal)

#### Floor

- Same as cap but applies if interest rates fall *below* strike

### Options (nonlinear)

- A contract that gives the right but not obligation to buy/sell an underlying asset at a specified strike price on or before the expiry, depending on the option formed.

### Futures (linear)

- A contract that obligates the buyer to buy and seller to sell the underlying asset at a set price on a set time in the future.
- Can be used to hedge against price volatility
- Reflects expectation of market
- Spot price: current market price for underlying asset
- Futurs price: Price set for futures delivery

### Swaps (linear)

- Derivative contract where two parties exchange cash flows from 2 different financial instruments.
- Fixed to floating (vanilla swap)
- Floating to floating (basis swap)
- Notional principal: Hypothetical underlying amount to calculate interest. Not actually exchanged.
- **Terms are highly customizable and swaptions exist.**
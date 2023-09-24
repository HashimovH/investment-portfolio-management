export default function Statistics({ currentBalance = 0, totalProfitLoss = 0, totalPortfolioValue = 0 }) {
    return (
        <section className="general-information container">
            <h4 className="section-header">General Information</h4>
            <div className="row gx-3">
                <div className="col-md-4">
                    <div className="bg-gray border-radius stat-block">
                        <p>Current Balance</p>
                        <h2>€ {currentBalance}</h2>
                    </div>

                </div>
                <div className={`col-md-4`}>
                    <div className="bg-gray border-radius stat-block">
                        <p>Total Profit/Loss</p>
                        <h2 className={`${totalProfitLoss > 0 ? 'text-success' : totalProfitLoss < 0 ? 'text-danger' : ''}`}>€ {totalProfitLoss}</h2>
                    </div>
                </div>
                <div className="col-md-4">
                    <div className="bg-gray border-radius stat-block">
                        <p>Total Portfolio Value</p>
                        <h2>€ {totalPortfolioValue}</h2>
                    </div>

                </div>
            </div>
        </section>
    )
}
export default function Sidebar({ recentStocks, mostProfitableClients }) {
    return (
        <div className="sidebar">
            <div className="d-flex mb-3">
                <h5 className="m-0">Recent Stocks</h5>
            </div>
            <div className="list-group list-group-flush">
                {recentStocks.map((stock, index) => (
                    <div key={index} className="list-group-item d-flex justify-content-between bg-gray border-radius mb-2 text-gray">
                        <span className="item-text">{stock.name}</span>
                        <span className="item-text">€ {stock.price}</span>
                    </div>
                ))}
            </div>
            <div className="d-flex mb-3 mt-5">
                <h5 className="m-0">Most Profitable Clients</h5>
            </div>
            <div className="list-group list-group-flush">
                {mostProfitableClients.map((client, index) => (
                    <div key={index} className="list-group-item d-flex justify-content-between bg-gray border-radius mb-2 text-gray">
                        <span className="item-text">{client.name}</span>
                        <span className="item-text">€ {client.profit}</span>
                    </div>
                ))}

            </div>
        </div>
    );
}
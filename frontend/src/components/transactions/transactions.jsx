import { useState } from "react";
import PurchaseModal from "./purchaseModal";

export default function Transactions({ transactions = [], stockOptions = [] }) {
    const [showModal, setShowModal] = useState(false);

    const handleCreatePurchase = () => {
        console.log("Create Purchase");
        setShowModal(true);
    };

    const handleCloseModal = () => {
        setShowModal(false);
    };
    return (
        <div className="container mt-5">
            <div className="d-flex justify-content-between align-items-center mb-3">
                <h5>Transactions</h5>
                <button className="btn btn-secondary btn-sm" onClick={handleCreatePurchase}>Create New Purchase</button>
            </div>
            <table className="table table-gray">
                <thead>
                    <tr>
                        <th>Stock</th>
                        <th>Volume</th>
                        <th>Purchase Price</th>
                        <th>Current Price</th>
                        <th>Gain/Loss</th>
                        <th>Purchase Time</th>

                    </tr>
                </thead>
                <tbody>
                    {transactions.map((transaction) => (
                        <tr key={transaction.id}>
                            <td className="text-gray">{transaction.stock}</td>
                            <td className="text-bold">{transaction.volume}</td>
                            <td className="text-bold">{transaction.purchasePrice}</td>
                            <td className="text-bold">{transaction.currentPrice}</td>
                            <td>{transaction.gainOrLoss}</td>
                            <td className="text-gray">{transaction.purchaseTime}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            {showModal && (
                <PurchaseModal handleCloseModal={handleCloseModal} stockOptions={stockOptions} />
            )}
        </div>

    );
}
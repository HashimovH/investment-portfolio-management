import { useEffect, useState } from "react";
import PurchaseModal from "./purchaseModal";
import axios from "axios";
import config from "../../config";

export default function Transactions({ stockOptions = [] }) {
    const [showModal, setShowModal] = useState(false);
    const [formData, setFormData] = useState({ stock_id: '', volume: '' });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const createTransaction = async () => {
        try {
            const token = localStorage.getItem('token');
            const data = {
                stock: formData.stock_id,
                volume: formData.volume
            };
            const response = await axios.post(`${config.API_URL}/api/transactions`, data, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            console.log('Transaction created:', response.data);
            setShowModal(false);
            getTransactions();
            return response.data;
        } catch (error) {
            console.error('Error creating transaction:', error.response ? error.response.data : error.message);
            throw new Error('Failed to create transaction');
        }
    };

    const handleCreatePurchase = () => {
        setShowModal(true);
    };

    const handleCloseModal = () => {
        setShowModal(false);
    };
    const handleSubmit = async (e) => {
        e.preventDefault();
        createTransaction();
    };

    const [transactions, setTransactions] = useState([]);
    const getTransactions = async () => {
        try {
            const token = localStorage.getItem('token');

            const response = await axios.get(`${config.API_URL}/api/transactions`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            console.log('Transactions:', response.data);
            setTransactions(response.data);
        } catch (error) {
            console.error('Error fetching transactions:', error.response ? error.response.data : error.message);
        }
    }
    useEffect(() => {
        getTransactions();
    }, []);
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
                            <td className="text-bold">€ {transaction.purchase_price}</td>
                            <td className="text-bold">{transaction.currentPrice}</td>
                            <td>{transaction.gainOrLoss}</td>
                            <td className="text-gray">{transaction.purchase_date}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            {showModal && (
                <PurchaseModal handleCloseModal={handleCloseModal} stockOptions={stockOptions} handleInputChange={handleInputChange} handleSubmit={handleSubmit} />
            )}
        </div>

    );
}
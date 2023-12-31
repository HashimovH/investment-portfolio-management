import React from "react";
import { useEffect, useState } from "react";
import PurchaseModal from "./PurchaseModal";
import axios from "axios";
import config from "../../config";

export default function Transactions({ stockOptions = [], setTotalGain, setTotalValue, setBalance }) {
    const [showModal, setShowModal] = useState(false);
    const [formData, setFormData] = useState({ stock_id: '', volume: '' });
    const [errorMessage, setErrorMessage] = useState(null);
    const [transactions, setTransactions] = useState([]);

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
            if (response.status === 201) {
                console.log('Transaction created:', response.data);
                setShowModal(false);
                getTransactions();
                setErrorMessage(null);
                setBalance(response.data.balance);
                return response.data;
            } else {
                console.error('Error creating transaction:', response.data);
                setErrorMessage('Failed to create transaction. ', response.data);
            }

        } catch (error) {
            console.error('Error creating transaction:', error.response ? error.response.data : error.message);
            setErrorMessage(`Failed to create transaction. ${error.response ? error.response.data.detail : error.message.detail}`);
            if (error.response && error.response.status === 401) {
                window.location.href = '/login';
            }
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

    const getTransactions = async () => {
        try {
            const token = localStorage.getItem('token');

            const response = await axios.get(`${config.API_URL}/api/transactions`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            console.log('Transactions:', response.data);
            setTransactions(response.data.transactions);
            setTotalGain(response.data.total_gain);
            setTotalValue(response.data.total_value);
        } catch (error) {
            console.error('Error fetching transactions:', error.response ? error.response.data : error.message);
            if (error.response && error.response.status === 401) {
                window.location.href = '/login';
            }
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
                            <td className="text-bold">€ {transaction.current_price}</td>
                            <td className={transaction.gain > 0 ? 'text-bold text-success' : transaction.gain < 0 ? 'text-bold text-danger' : 'text-bold'}>
                                {transaction.gain > 0 ? '+' : (transaction.gain < 0 ? '-' : '')} € {Math.abs(transaction.gain)}
                            </td>
                            <td className="text-gray">{transaction.purchase_date}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            {showModal && (
                <PurchaseModal handleCloseModal={handleCloseModal} stockOptions={stockOptions} handleInputChange={handleInputChange} handleSubmit={handleSubmit} errorMessage={errorMessage} />
            )}
        </div>

    );
}
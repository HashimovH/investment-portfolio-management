import axios from "axios";
import Header from "../header";
import Sidebar from "../sidebar/sidebar";
import Statistics from "../statistics";
import Transactions from "../transactions/transactions";
import config from "../../config";
import { useEffect, useState } from "react";


export default function Home() {
    const [currentUser, setCurrentUser] = useState({});
    const [stocks, setStocks] = useState([]);
    const [totalGain, setTotalGain] = useState(0);
    const [totalValue, setTotalValue] = useState(0);
    const [balance, setBalance] = useState(0);
    const getCurrentUser = async () => {
        try {
            const token = localStorage.getItem('token');

            const response = await axios.get(`${config.API_URL}/api/me`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            console.log('Current user:', response.data);
            setBalance(response.data.balance)
            setCurrentUser(response.data);
        } catch (error) {
            console.error('Error fetching current user:', error.response ? error.response.data : error.message);
        }
    };
    const getStocks = async () => {
        try {
            const token = localStorage.getItem('token');

            const response = await axios.get(`${config.API_URL}/api/stocks`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            console.log('Stocks:', response.data);
            setStocks(response.data);
        } catch (error) {
            console.error('Error fetching stocks:', error.response ? error.response.data : error.message);
            if (error.response && error.response.status === 401) {
                window.location.href = '/login';
            }
        }
    }

    useEffect(() => {
        getCurrentUser();
        getStocks();
    }, []);
    return (
        <div>
            <Header first_name={currentUser.name} last_name={currentUser.surname} />
            <div className='row'>
                <div className='col-md-8'>
                    <Statistics currentBalance={balance} totalProfitLoss={totalGain} totalPortfolioValue={totalValue} />
                    <Transactions stockOptions={stocks} setTotalGain={setTotalGain} setTotalValue={setTotalValue} setBalance={setBalance} />
                </div>
                <div className='col-md-4'>
                    <Sidebar recentStocks={stocks} />
                </div>
            </div>
        </div>
    )
}
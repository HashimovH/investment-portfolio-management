import Header from "../header";
import Sidebar from "../sidebar/sidebar";
import Statistics from "../statistics";
import Transactions from "../transactions/transactions";

export default function Home() {
    const stocks = [
        { company: "Adcash OU", price: "5.00" },
        { company: "Wise OU", price: "4.00" },
        { company: "Transferwise OU", price: "3.00" },
    ];
    const clients = [
        { name: "Hashim Hashimov", profit: "3200" },
        { name: "Hashim Hashimov", profit: "3200" },
        { name: "Hashim Hashimov", profit: "3200" },
    ]
    return (
        <div>
            <Header first_name={"Hashim"} last_name={"Hashimov"} />
            <div className='row'>
                <div className='col-md-8'>
                    <Statistics />
                    <Transactions />
                </div>
                <div className='col-md-4'>
                    <Sidebar recentStocks={stocks} mostProfitableClients={clients} />

                </div>
            </div>
        </div>
    )
}
/**
 * A user qualifies if ALL of the following conditions are met:

Has made at least 50 transactions in the last 6 months
Has spent a total of more than $5,000 in the last 6 months
Has no missed payments in the last 12 months
 */

type TransactionType = "RECEIVED" | "SPENT"

interface Transaction {
    transactionId: string,
    createdAt: Date,
    amount: number,
    type: TransactionType
}

interface MissedPaymentReport {
    missedPaymentId: string,
    createdAt: Date
}

interface User {
    user_id: string,
    name: string,
    transactions: Transaction[],
    missedPayments: MissedPaymentReport[]
}
interface Transaction {
    type: TransactionType,
    amount: number,
    timestamp: number,
    target_account_id: String
}

/**
 * Can be upgraded to more types
 */
enum TransactionType {
    TRANSFERENCE,
}

const INVALID_OPERATION_MSG = "Invalid operation."
const INVALID_OPERATION_SAME_ACCOUNT_TRANSFER = "Invalid operation. The Sender and Receivers' IDs are the same."
class Account {
    public account_id: string;
    private balance: number = 0;
    private transaction_history: Array<Transaction> = [];
    name: string;

    constructor(name: string, account_id: string) {
        this.name = name;
        this.account_id = account_id;
    }

    public deposit(amount: number) {
        if (amount < 0) {
            throw new Error(INVALID_OPERATION_MSG)
        }
        this.balance += amount;
    }

    public addTransaction(type: TransactionType, amount: number, target_account_id: string) {
        const transaction: Transaction = {
            type: type,
            amount: amount,
            timestamp: new Date().getTime(),
            target_account_id: target_account_id
        }
        this.transaction_history.push(transaction);
    }

    public withdraw(amount: number) {
        if (amount > this.balance) {
            throw new Error("It is not possible to withdraw the amount you've requested. Please try with a different amount.");
        }
        if (amount < 0) {
            throw new Error(INVALID_OPERATION_MSG)
        }
        // todo: add extra withdrawal logic
        this.balance -= amount;
    }

    public get_balance() {
        return this.balance;
    }

    public get_transactions() {
        return this.transaction_history;
    }
}

class Bank {
    public accounts = new Map<string, Account>();

    /**
     * Create a new account
     * @param name The name of the new account
     */
    public create_account(name: string): string {
        const acc_id = crypto.randomUUID();
        const newAccount = new Account(name, acc_id);
        this.accounts.set(acc_id, newAccount);
        return acc_id;
    }

    public get_account(account_id: string): Account {
        const foundAcc = this.accounts.get(account_id);
        if (!foundAcc) throw new Error("Account not found");
        return foundAcc;
    }

    public transfer(from_id: string, to_id: string, amount: number) {
        if (amount < 0) {
            throw new Error(INVALID_OPERATION_MSG)
        }
        if (from_id == to_id) {
            throw new Error(INVALID_OPERATION_SAME_ACCOUNT_TRANSFER)
        }

        const from_acc = this.get_account(from_id);
        const to_acc = this.get_account(to_id);

        // ?? Could add logic / new messages for each case.
        if (!from_acc || !to_acc) {
            throw new Error("One of the accounts couldn't be found. Please try again later.")
        }


        from_acc.withdraw(amount);
        to_acc.deposit(amount);


        /**
         * The accounts we've deposited from and to.
         */
        from_acc.addTransaction(
            TransactionType.TRANSFERENCE,
            amount,
            to_id
        )
        to_acc.addTransaction(
            TransactionType.TRANSFERENCE,
            amount,
            to_id
        )
    }
}

const banamex = new Bank()
const andresID = banamex.create_account("Andres")
const sofiaID = banamex.create_account("Sofia")

const andresAcc = banamex.get_account(andresID);
const sofiaAcc = banamex.get_account(sofiaID);

if (andresAcc && sofiaAcc) {
    andresAcc.deposit(100);
    console.log(andresAcc.get_balance())

    banamex.transfer(andresID, sofiaID, 50);

    console.log(andresAcc.get_balance()) // should be 50
    console.log(sofiaAcc.get_balance()) // should be 50
}

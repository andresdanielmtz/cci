/**
3 Types of Users
Any of them can get the Gold Card 

Gold Card:
- Only if user has the following conditions:
    - More than 5 years 
    - More than 600 points in credit card score 
    - Have no debts within the last year

Create a structure that would facilitate the most if the candidate can or not obtain this card. Should be reutilized for other calculations.

This structure should represent the user's data.
*/

interface DebtOcurrence {
    debt_id: String,
    createdAt: Date
}

interface User {
    id: String
    name: String,
    createdAt: Date,
    creditScore: number,
    debtOcurrences: DebtOcurrence[]
}

const example: User = {
    id: "123",
    name: "Andres",
    createdAt: new Date(1586051667935),
    creditScore: 700,
    debtOcurrences: [
        {
            debt_id: "123",
            createdAt: new Date(1743817774152)
        }
    ]
}

const hasDebtOccurrencedHappenedWithLastYear = (debts: DebtOcurrence[]) => {
    const todayDate = new Date();
    const todayYear = todayDate.getFullYear();

    const oneYearAgoDate = new Date();
    oneYearAgoDate.setFullYear(todayYear - 1);
    
    const todayDateTimestamp = todayDate.getTime();
    const oneYearAgoDateTimestamp = oneYearAgoDate.getTime();

    for (let debt of debts) {
        const debtTimestamp = debt.createdAt.getTime();

        if (oneYearAgoDateTimestamp <= debtTimestamp && debtTimestamp <= todayDateTimestamp) {
            return true;
        }
    }
    return false;
}


const isEligibleToGoldCard = (user: User) => {
    const todayDate = new Date(); // By default it is today

    const userAgeMinimum = 5; // The user should've been registered for more than 5 years.
    const hasUserBeenMoreThan5Years = todayDate.getFullYear() - user.createdAt.getFullYear() >= userAgeMinimum;

    console.log(todayDate.getFullYear())
    console.log(user.createdAt.getFullYear())

    const minimumCreditScore = 600;
    const isUserCreditScoreEnough = user.creditScore >= minimumCreditScore;

    const isDebtRegisteredWithinLastYear = hasDebtOccurrencedHappenedWithLastYear(user.debtOcurrences);

    return hasUserBeenMoreThan5Years && isUserCreditScoreEnough && !isDebtRegisteredWithinLastYear;
}

const isUserEligible = isEligibleToGoldCard(example);
console.log(isUserEligible);
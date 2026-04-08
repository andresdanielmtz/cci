const date = new Date()
const date6YearsAgo = new Date();
date6YearsAgo.setFullYear(date.getFullYear - 6);

console.log(date6YearsAgo.getTime()) // 1586051667935 
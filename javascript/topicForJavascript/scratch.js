let ride = new Promise((resolve, reject) => {
    if (arrived) {
        resolve('Driver arrived.');
    } else {
        reject("Driver bailed.");
    }
})

ride.then(value => {
    console.log(value);
    // Driver arrived
}).catch(error => {
    console.log(error);
}).finally(() => {
    console.log("bala bala")
})
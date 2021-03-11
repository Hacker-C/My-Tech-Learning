let num = 10;
function outer() {
    let num = 20;
    function inner() {
        console.log(num);
    }
    inner();
}
outer();
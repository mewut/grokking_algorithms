// моя

function personIsSeller(name) {
    return name.slice(-1) === 'm';
}

const graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
};

function search(name) {
    let searchQueue = [];
    let searched = [];
    searchQueue.push(name);
    while (searchQueue.length > 0) {
        let person = searchQueue.shift();
        if (!searched.includes(person)) {
            if (personIsSeller(person)) {
                console.log(person + ' is a mango seller!');
                return true;
            } else {
                graph[person].forEach(friend => {
                    if (!searched.includes(friend)) {
                        searchQueue.push(friend);
                    }
                });
                searched.push(person);
            }
        }
    }
    return false;
}

search('you');

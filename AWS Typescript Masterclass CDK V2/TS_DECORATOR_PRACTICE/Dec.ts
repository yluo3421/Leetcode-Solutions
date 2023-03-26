const someObject = {
    someProperty: 'initial'
}

class Manager {
    //@watchChange
    @linkValue(someObject)
    someProperty: string

}

const manager: Manager = new Manager();

manager.someProperty = '123';
console.log('someObject.someProperty = ' + someObject.someProperty)
manager.someProperty = '456';
console.log('someObject.someProperty = ' + someObject.someProperty)



function linkValue(otherObject: any) {
    return function(target: any, key: string) {
        let property = target[key];

    const getter = ()=>{
        return property
    };

    const setter = (newVal: any)=>{
        property = newVal;
        otherObject[key] = newVal
    };

    Object.defineProperty(target, key, {
        get: getter,
        set: setter,
        configurable: true,
        enumerable: true
    })
    }
}

function watchChange(target: any, key: string){
    // target is the Manager class itsel
    // key is the name of our property
    
    let property = target[key];

    const getter = ()=>{
        return property
    };

    const setter = (newVal: any)=>{
        property = newVal;
        console.log(`${key as string} changed from ${property} to ${newVal}`)
    };

    Object.defineProperty(target, key, {
        get: getter,
        set: setter,
        configurable: true,
        enumerable: true
    })
}
function App() {
    
  
    return (
      <div>
        <NavComponent />
        <Switch>
          <Route exact path="/">
            <HomePage user = {user}/>
          </Route>
          
  
        </Switch>
      </div>
    );
  }
  
  export default App;
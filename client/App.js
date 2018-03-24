import React, {Component} from 'react';

import { StackNavigator } from 'react-navigation';

import Home from './screens/Home';
import Form from './screens/Form';

const App = StackNavigator({
  Home: { screen: Home },
  Form: {screen: Form},
},{
  initialRouteName: 'Home',
});

export default App;

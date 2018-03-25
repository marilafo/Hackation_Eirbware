import React, {Component} from 'react';
import { ScrollView, StyleSheet, Text, View, Picker } from 'react-native';
import { TextField } from 'react-native-material-textfield';
import SubmitButton from '../elements/buttons/SubmitButton';
import CancelButton from '../elements/buttons/CancelButton';
import SocketIOClient from 'socket.io-client';

export default class Form extends Component {
  static navigationOptions = {
    header: null,
  }

  constructor(props) {
      super(props);

      this.onFocus = this.onFocus.bind(this);
      this.onSubmit = this.onSubmit.bind(this);
      this.onChangeText = this.onChangeText.bind(this);
      this.onSubmitName = this.onSubmitName.bind(this);
      this.onSubmitFirst = this.onSubmitFirst.bind(this);
      this.onSubmitSecond = this.onSubmitSecond.bind(this);
      this.onSubmitThird = this.onSubmitThird.bind(this);
      this.onSubmitFourth = this.onSubmitFourth.bind(this);
      this.onSubmitFifth = this.onSubmitFifth.bind(this);

      this.nameRef = this.updateRef.bind(this, 'name');
      this.firstRef = this.updateRef.bind(this, 'first');
      this.secondRef = this.updateRef.bind(this, 'second');
      this.thirdRef = this.updateRef.bind(this, 'third');
      this.fourthRef = this.updateRef.bind(this, 'fourth');
      this.fifthRef = this.updateRef.bind(this, 'fifth');


      this.state = {
        name: '',
        first : '',
        second : '',
        third : '',
        fourth : '',
        fifth : '',
        hair: '',
        eyes: '',
        sex: '',
      };
    }

    onFocus() {
      let { errors = {} } = this.state;

      for (let name in errors) {
        let ref = this[name];

        if (ref && ref.isFocused()) {
          delete errors[name];
        }
      }

      this.setState({ errors });
    }

    onChangeText(text) {
      ['name', 'first', 'second', 'third', 'fourth','fifth']
        .map((name) => ({ name, ref: this[name] }))
        .forEach(({ name, ref }) => {
          if (ref.isFocused()) {
            this.setState({ [name]: text });
          }
        });
    }

    onSubmitName() {
      this.first.focus();
    }

    onSubmitFirst() {
      this.second.focus();
    }

    onSubmitSecond() {
      this.third.focus();
    }

    onSubmitThird() {
      this.fourth.focus();
    }

    onSubmitFourth() {
      this.fifth.focus();
    }

    onSubmitFifth() {
      this.fifth.blur();
    }

    onReady() {
      console.log("here you can handle connection and then navigation to the next screen");
      socket = SocketIOClient('https://eirbware-hackathon.herokuapp.com:80');

      socket.on("connect", () => {
          console.log("connected");
          socket.emit("info", this.state);
          // go to mini games
        }
      )
    }

    onSubmit() {
      let errors = {};
      let count = 0;

      ['name', 'first', 'second', 'third', 'fourth','fifth']
      .forEach((name) => {
        let value = this[name].value();

        if (!value) {
          errors[name] = 'Should not be empty';
          count ++;
        }
      });

      this.setState({ errors });

      if(count == 0){
        this.onReady();
      }
    }

    updateRef(name, ref) {
      this[name] = ref;
    }

  render(){
    let { errors = {}, secureTextEntry, ...data } = this.state;
    let { firstname = 'name', lastname = 'house' } = data;
    return(
      <View style={{flex:1,backgroundColor: '#fff'}}>
        <ScrollView
          style={styles.scroll}
          contentContainerStyle={styles.contentContainer}
          keyboardShouldPersistTaps='handled'>
          <View style={styles.container}>
            <View style={styles.placeTitle}>
              <Text style={styles.title}>Please fill in these informations</Text>
            </View>

            <TextField
              ref={this.nameRef}
              value={data.name}
              autoCorrect={false}
              enablesReturnKeyAutomatically={true}
              onFocus={this.onFocus}
              onChangeText={this.onChangeText}
              onSubmitEditing={this.onSubmitName}
              returnKeyType='next'
              label='Name'
              error={errors.name}
            />

            <TextField
              ref={this.firstRef}
              value={data.about}
              onFocus={this.onFocus}
              onChangeText={this.onChangeText}
              onSubmitEditing={this.onSubmitFirst}
              returnKeyType='next'
              multiline={true}
              blurOnSubmit={true}
              label='First Clue'
              characterRestriction={140}
              error={errors.first}
            />

            <TextField
              ref={this.secondRef}
              value={data.about}
              onFocus={this.onFocus}
              onChangeText={this.onChangeText}
              onSubmitEditing={this.onSubmitSecond}
              returnKeyType='next'
              multiline={true}
              blurOnSubmit={true}
              label='Second Clue'
              characterRestriction={140}
              error={errors.second}
            />

            <TextField
              ref={this.thirdRef}
              value={data.about}
              onFocus={this.onFocus}
              onChangeText={this.onChangeText}
              onSubmitEditing={this.onSubmitThird}
              returnKeyType='next'
              multiline={true}
              blurOnSubmit={true}
              label='Third Clue'
              characterRestriction={140}
              error={errors.third}
            />

            <TextField
              ref={this.fourthRef}
              value={data.about}
              onFocus={this.onFocus}
              onChangeText={this.onChangeText}
              onSubmitEditing={this.onSubmitFourth}
              returnKeyType='next'
              multiline={true}
              blurOnSubmit={true}
              label='Fourth Clue'
              characterRestriction={140}
              error={errors.fourth}
            />

            <TextField
              ref={this.fifthRef}
              value={data.about}
              onFocus={this.onFocus}
              onChangeText={this.onChangeText}
              onSubmitEditing={this.onSubmitFifth}
              returnKeyType='next'
              multiline={true}
              blurOnSubmit={true}
              label='Fifth Clue'
              characterRestriction={140}
              error={errors.fifth}
            />
          <Text>Hair:</Text>
          <Picker
            selectedValue = {this.state.hair}
            onValueChange={(itemValue, itemIndex) => this.setState({hair: itemValue})}>
            <Picker.Item label="Blond" value="blond" />
            <Picker.Item label="Brown" value="brown" />
            <Picker.Item label="Red" value="red" />
            <Picker.Item label="White" value="white" />
            <Picker.Item label="No Hair" value="noHair" />
          </Picker>

          <Text>Eyes:</Text>
          <Picker
            selectedValue = {this.state.eyes}
            onValueChange={(itemValue, itemIndex) => this.setState({eyes: itemValue})}>
            <Picker.Item label="Blue" value="blue" />
            <Picker.Item label="Brown" value="brown" />
            <Picker.Item label="Green" value="green" />
            <Picker.Item label="Wall eyes" value="wall" />
          </Picker>

          <Text>Sex:</Text>
          <Picker
            selectedValue = {this.state.sex}
            onValueChange={(itemValue, itemIndex) => this.setState({sex: itemValue})}>
            <Picker.Item label="Female" value="female" />
            <Picker.Item label="Male" value="male" />
            <Picker.Item label="Undefined" value="undefined" />
          </Picker>

          </View>

          <View style={styles.containerButton}>
            <CancelButton
              onPress = { () => this.props.navigation.goBack()}
              />
            <SubmitButton
              onPress = {this.onSubmit}
              />
          </View>

        </ScrollView>
      </View>
    );
  }
}
const styles = StyleSheet.create({
  placeTitle: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 40,
    fontWeight: 'bold',
    color: '#1c73ff',
    textAlign: 'center',
  },
  scroll: {
    backgroundColor: '#E8EAF6',
  },

  container: {
    margin: 8,
    marginTop: 24,
  },

  containerButton: {
    margin: 8,
    marginTop: 24,
    flexDirection: 'row',
  },

  contentContainer: {
    padding: 8,
},
});

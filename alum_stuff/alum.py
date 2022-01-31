class Alum:
    def __init__ (self):
        self._first_name = ""
        self._last_name = ""
        self._cohort_year = 0
        self._major = ""
        self._city = ""
        self._state = ""
        self._company = ""
        self._email = ""
        self._position = ""
        self._update = ""
    
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    
    @property
    def cohort_year(self):
        return self._cohort_year 
    
    @cohort_year.setter
    def cohort_year(self, value):
        self._cohort_year = value

    @property
    def major(self):
        return self._major
    
    @major.setter
    def major(self, value):
        self._major = value
    
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
    
    @property
    def company(self):
        return self._company
    
    @company.setter
    def company(self, value):
        self._company = value
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        self._position = value
   
    @property
    def update(self):
        return self._update
    
    @update.setter
    def update(self, value):
        self._update = value



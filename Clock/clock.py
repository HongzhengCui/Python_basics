class MyClock24:
    def __init__(self, hours, minutes, seconds):
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError("Please provide the valid parameters.S")
        
        self.hours = hours
        self.minutes = minutes
        self. seconds = seconds
        self.total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
    
        
    @property
    def valid_hour(self):
        self.hours  = self.total_seconds // 3600
        
        return self.hours
    
    
    @property
    def valid_minute(self):
        self.minutes = (self.total_seconds % 3600) // 60
        
        return self.minutes
    
    
    @property
    def valid_second(self):
        self.seconds = (self.total_seconds % 3600) % 60
            
        return self.seconds
    
    
    def tick(self):
        self.seconds += 1
        
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                
                if self.hours == 24:
                    self.hours = 0


    def __str__(self):
        
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)


    def __repr__(self):
        clock_info = {'hours': self.hours, 'minutes': self.minutes, 'seconds': self.seconds}
        return str(clock_info)


    def __eq__(self, other):
        if isinstance(other, MyClock24):
            return self.total_seconds == other.total_seconds
        
        return False


    def __ne__(self, other):
        
        return not self.__eq__(other)


    def __ge__(self, other):
        if isinstance(other, MyClock24):
            
            return self.total_seconds >= other.total_seconds
        
        return NotImplemented


    def __gt__(self, other):
        if isinstance(other, MyClock24):
            
            return self.total_seconds > other.total_seconds
        
        return NotImplemented


    def __le__(self, other):
        if isinstance(other, MyClock24):
            
            return self.total_seconds <= other.total_seconds
        
        return NotImplemented


    def __lt__(self, other):
        if isinstance(other, MyClock24):
            
            return self.total_seconds < other.total_seconds
        
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, MyClock24):
            total_seconds = (self.total_seconds + other.total_seconds) % (24 * 3600)
            
            return MyClock24(total_seconds // 3600, (total_seconds // 60) % 60, total_seconds % 60)
        
        elif isinstance(other, int):
            total_seconds = (self.total_seconds + other) % (24 * 3600)
            
            return MyClock24(total_seconds // 3600, (total_seconds // 60) % 60, total_seconds % 60)
        
        else:
            
            return NotImplemented


    def __sub__(self, other):
        if isinstance(other, MyClock24):
            total_seconds = (self.total_seconds - other.total_seconds) % (24 * 3600)
            
            return MyClock24(total_seconds // 3600, (total_seconds // 60) % 60, total_seconds % 60)
        
        elif isinstance(other, int):
            total_seconds = (self.total_seconds - other) % (24 * 3600)
            
            return MyClock24(total_seconds // 3600, (total_seconds // 60) % 60, total_seconds % 60)
        
        else:
            
            return NotImplemented
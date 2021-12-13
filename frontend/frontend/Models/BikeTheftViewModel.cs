using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace frontend.Models
{
    public class BikeTheftViewModel
    {
        public int Occurence_Hour { get; set; }
        public int Bike_Speed { get; set; }
        public int Cost_of_Bike { get; set; }
        public int Report_Lag { get; set; }
        public int Primary_Offence_THEFT { get; set; }
    }
}
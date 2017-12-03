// -- BEGIN LICENSE BLOCK ----------------------------------------------
// -- END LICENSE BLOCK ------------------------------------------------
//----------------------------------------------------------------------
/*!\file
 *
 * \author  Christoph Rist <rist.christoph@gmail.com>
 * \date    2017-12-01
 *
 */
//----------------------------------------------------------------------

#include <algorithm>
#include <iostream>
#include <fstream>
#include <iomanip>


void work(std::istream &input, std::ostream &output)
{
  size_t num_test_cases;
  input >> num_test_cases;

  std::string line;
  // read only \n
  getline(input, line);

  uint32_t total_sum = 0;

  output << "hello\n";
}



int main(int argc, char** argv)
{
  //! if arguments are specified, treat them as files to read from/write to
  std::ifstream f_in{};
  std::ofstream f_out{};
  if (argc <= 1)
  {
    work(std::cin, std::cout);
  }
  else if (argc > 2)
  {
    f_out.open(argv[2]);
    if (!f_out.good())
      return 1;
    work(f_in, f_out);
  }
  else
  {
    f_in.open(argv[1]);
    if (!f_in.good())
      return 1;
    work(f_in, std::cout);
  }
  return 0;
}
